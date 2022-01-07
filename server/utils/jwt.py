from typing import Dict
from datetime import datetime, timedelta
import os
from jose import jwt
import dotenv
dotenv.load_dotenv()
class JWTManager:
    @staticmethod
    def sign(user: str) -> Dict[str, str]:
        """signs a jwt on the user"""
        headers: dict = {
            "alg": "HS256",
        }
        payload: dict = {
            "user": user,
            "exp": datetime.utcnow() + timedelta(days=1),
            "iss": os.getenv("base_url"),
            "sub": "auth",
            "aud": "platypus",
            "iat": datetime.utcnow(),
        }
        token: str = jwt.encode(payload, os.getenv("jwt_secret"), headers=headers)
        print(token)


    @staticmethod
    def dec(token: str) -> Dict[str, str]:
        """decodes a jwt"""
        try:
            payload: dict = jwt.decode(token, os.getenv("JWT_SECRET"), algorithms=["HS256"])
            return payload if payload["expires"] > datetime.utcnow() else None
        except:
            return None


token = JWTManager.sign("test")
# print(token)
# print(JWTManager.dec(token["access_token"]))
