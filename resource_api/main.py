from fastapi import FastAPI, Depends

from auth_service import get_current_user
from models import Resource, User
from resource_service import ResourceService, get_resource_service

app = FastAPI()


@app.get("/resources", response_model=list[Resource])
def read_item(user: User = Depends(get_current_user),
              resource_service: ResourceService = Depends(
                  get_resource_service)) -> list[Resource]:
    """
    An endpoint for retrieving a list of resources
    :param user:
    :param resource_service:
    :return:
    """
    resources = resource_service.get_resources()
    return resources
