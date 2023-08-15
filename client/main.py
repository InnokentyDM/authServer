import requests
from settings import settings
from requests.auth import HTTPBasicAuth


def get_resources():
    """
    A simple example of accessing resources and using auth service.
    In general, it can be any type of client (e.g. mobile, another api, web)
    :return:
    """
    print('Retrieving access token')
    access_token_url = f'{settings.auth_api_url}/token'
    access_token = requests.get(access_token_url,
                                auth=HTTPBasicAuth('User', 'Password'))
    print('Access token is retrieved')
    print('Retrieving resources')
    resources_url = f'{settings.resource_api_url}/resources'
    response = requests.get(resources_url, headers={'Authorization':
                                                         f'Bearer {access_token}'})
    resources = response.json()
    print('Resources are retrieved')
    print(resources)
    return resources


if __name__ == '__main__':
    get_resources()
