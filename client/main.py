import requests
from settings import settings
from requests.auth import HTTPBasicAuth


def get_resources():
    """
    A simple example of accessing resources and using auth service.
    In general, it can be any type of client (e.g. mobile, another api, web)
    :return:
    """
    access_token_url = f'{settings.auth_api_url}/token'

    access_token = requests.get(access_token_url,
                                auth=HTTPBasicAuth('User', 'Password'))
    resources_url = f'{settings.resource_api_url}/resources'
    resources = requests.get(resources_url, headers={'Authorization':
                                                         f'Bearer {access_token}'})
    print(resources)
    return resources


if __name__ == '__main__':
    get_resources()
