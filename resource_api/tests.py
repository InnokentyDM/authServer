from fastapi.testclient import TestClient
from resource_api.main import app

client = TestClient(app)


def test_get_resources():
    """
    Test retrieving a list of resources
    :return:
    """
    headers = {
        'Authorization': 'Bearer test'
    }
    response = client.get("/resources", headers=headers)
    assert response.status_code == 200
    assert len(response.json()) == 3
    data = response.json()
    assert data[0]['title'] == "Resource 1"
    assert data[1]['title'] == "Resource 2"
    assert data[2]['title'] == "Resource 3"


def test_get_resources_unauthorized_access():
    """
    Test attempt of unauthorized access
    :return:
    """
    response = client.get("/resources")
    assert response.status_code == 403
