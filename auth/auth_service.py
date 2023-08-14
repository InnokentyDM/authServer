from functools import lru_cache

from fastapi import status

from fastapi import HTTPException


class AuthService:
    """
    Authorization service check if the user is registered and generates
    an access token.
    """

    def get_access_token(self, username: str, password_hash: str) -> str:
        """
        This method generates checks if the user is registered and if the
        provided password hash is the same, then generates an access token.
        :param username:
        :param password_hash:
        :return: str
        """
        hardcoded_user = {"username": "User", "hashed_password": "Password"}

        if username != hardcoded_user["username"] or password_hash != \
                hardcoded_user['hashed_password']:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                detail="Incorrect username or password")

        return f'{username}:{password_hash}'


@lru_cache
def get_auth_service() -> AuthService:
    return AuthService()
