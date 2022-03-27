from fastapi import HTTPException
from fastapi.security import HTTPBasicCredentials
from app.db import database


async def check_credentials(credentials: HTTPBasicCredentials):
    """
    Check user authentication credentials

    :param credentials: user credentials
    :return: True if auth succeded
    :raises HTTPException: not authenticated
    """
    authenticated = await database.execute(
        query=(
            "SELECT EXISTS("
            "SELECT id FROM users "
            f"WHERE username = '{credentials.username}' "
            f"AND password = '{credentials.password}'"
            ")"
        )
    )

    if not authenticated:
        raise HTTPException(status_code=403)

    return True
