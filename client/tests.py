from main import get_resources


def test_get_resources():
    """
    Test retrieving a list of resources
    :return:
    """
    data = get_resources()
    assert data[0]['title'] == "Resource 1"
    assert data[1]['title'] == "Resource 2"
    assert data[2]['title'] == "Resource 3"
