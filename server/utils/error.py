from fastapi.responses import JSONResponse
import typing

class PlatyHTTPException(JSONResponse):
    def __init__(self, status: int, typ: str, title: str,  detail: str = None) -> None:
        super().__init__(
            content={
                "type": typ,
                "title": title,
                "detail": detail,
            },
            status_code=status,
            headers={"Content-Type": "application/problems+json"},
            media_type="application/problems+json",
            background=None,
        )
