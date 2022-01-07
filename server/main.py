import tempfile
from fastapi import FastAPI, File, UploadFile, Request
from fastapi.middleware.cors import CORSMiddleware
from minio import Minio
from minio.helpers import ObjectWriteResult
from dotenv import load_dotenv
import uuid
import os
import logging
from tortoise import Tortoise
from starlette.responses import FileResponse
# router
from server.routes.user import router as user_router

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
client: Minio = None
db = None
cursor = None


@app.post("/upload")
async def upload_file(req: Request, file: UploadFile = File(...)):
    # create temp file
    tmpfile = tempfile.NamedTemporaryFile(mode="w+b", prefix="sharx_")
    tmpfile.writelines(file.file.readlines())
    tmpfile.seek(0)
    # new upload
    uid = str(uuid.uuid4())
    cursor.execute(
        "INSERT INTO upload (uid, filename, mimetype, ip) VALUES (%s, %s, %s, %s)",
        (uid, file.filename, file.content_type, req.client.host),
    )
    db.commit()
    # write to minio
    result: ObjectWriteResult = client.fput_object(
        "sharx",
        uid,
        tmpfile.name,
        content_type=file.content_type,
    )
    # close file
    tmpfile.close()
    # return result name
    return result.object_name


@app.get("/download/{uid}")
async def download_file(uid: str):
    cursor.execute(
        "SELECT filename, mimetype FROM upload WHERE uid = %s",
        (uid,),
    )
    result = cursor.fetchone()
    client.fget_object(
        "sharx",
        uid,
        f"/tmp/sharx_{uid}",
    )
    resp = FileResponse(
        f"/tmp/sharx_{uid}",
        filename=result[0],
        media_type=result[1],
    )
    return resp


@app.on_event("startup")
async def startup():
    global client, db, cursor
    # load dotenv file
    load_dotenv()
    # connect to minio
    client = Minio(
        os.getenv("MINIO_ENDPOINT"),
        access_key=os.getenv("MINIO_ACCESS_KEY"),
        secret_key=os.getenv("MINIO_SECRET_KEY"),
        secure=False,
    )
    # create bucket if not exists sharx
    if not client.bucket_exists("sharx"):
        client.make_bucket("sharx")
    # connect to database using tortoise
    await Tortoise.init(db_url=os.getenv("DB_URL"), modules={"models": ["server.orm.models"]})
    await Tortoise.generate_schemas(safe=True)
    # create scheduler
    # scheduler = AsyncIOScheduler(timezone="Europe/Berlin")
    # scheduler.add_job(
    #     func=cleanup,
    #     trigger="interval",
    #     seconds=120,
    # )
    # scheduler.start()

app.include_router(user_router, prefix="/user")


def cleanup():
    logger = logging.getLogger("uvicorn")
    logger.info("Running cleanup...")
    files = []
    for file in os.listdir("/tmp"):
        if file.startswith("sharx_"):
            os.remove(f"/tmp/{file}")
            files.append(file)
            cursor.execute("DELETE FROM upload WHERE uid = %s", (file.split("_")[1],))
            db.commit()
    logger.info("Cleaned {} files".format(len(files)))
