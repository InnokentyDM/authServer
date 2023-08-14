from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from auth_service import get_auth_service, AuthService
from models import Token

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@app.post("/token", response_model=Token)
async def login_for_access_token(
        form_data: OAuth2PasswordRequestForm = Depends(), auth_service:
        AuthService = Depends(get_auth_service)):
    """
    An endpoint for validating user data and generating access token.
    
    **The username and password for testing are hardcoded 
    username: User
    password: Password
    :param form_data: 
    :param auth_service: 
    :return: 
    """
    token = auth_service.get_access_token(form_data.username,
                                          form_data.password)
    return {"access_token": token}
