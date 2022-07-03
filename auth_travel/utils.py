import datetime
import jwt
from django.conf import settings


def generate_access_token(usr):
    for user in usr:
        user_id = user.user_id
    access_token_payload = {
        "id": user_id,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(days=14),
        "iat": datetime.datetime.utcnow(),
    }
    access_token = jwt.encode(
        access_token_payload, settings.SECRET_KEY, algorithm="HS256"
    )

    return access_token


def generate_refresh_token(usr):
    for user in usr:
        user_id = user.user_id
    refresh_token_payload = {
        "id": user_id,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(days=60),
        "iat": datetime.datetime.utcnow(),
    }
    refresh_token = jwt.encode(
        refresh_token_payload, settings.REFRESH_TOKEN_SECRET, algorithm="HS256"
    )

    return refresh_token
