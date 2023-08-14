from functools import lru_cache
from fastapi import HTTPException, Depends
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from models import User

security = HTTPBearer()


class AuthService:
    """
    A class responsible for validation of Authorization token.
    Some additional logic can be also implemented here e.g. role-based access
    """

    def parse_token(self, token: str) -> str:
        """
        This method is dedicated for parsing to retrieve the user data
        :param token:
        :return:
        """
        return token

    def get_user(self, token: str) -> User:
        """
        Create a user object
        :param token:
        :return:
        """
        user_id = self.parse_token(token)
        return User(id=user_id)


@lru_cache
def get_auth_service() -> AuthService:
    """
    A dependency for using an AuthService
    :return:
    """
    return AuthService()


def get_current_user(
        authorization: HTTPAuthorizationCredentials = Depends(security),
        auth_service: AuthService = Depends(
            get_auth_service)) -> User:
    """
    A dependency for retrieving and parsing authorization request header
    and checking user permissions.
    :param request:
    :param auth_service:
    :return:
    """
    token = authorization.credentials

    if not token:
        raise HTTPException(status_code=401,
                            detail="Authorization header missing.")

    if token.startswith('Bearer '):
        token = token[7:]

    if not auth_service.parse_token(token):
        raise HTTPException(status_code=401, detail="Invalid token.")

    return auth_service.get_user(token)
