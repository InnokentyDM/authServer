from functools import lru_cache

from models import Resource


class ResourceService:
    """
    This is a mock resource service, in a real system it would contain logic
    related to resources (creating, reading, updating, deleting) and some
    more complex logic based on requirements
    """

    def get_resources(self) -> list[Resource]:
        """
        Retrieve a list of resources.
        Hardcoded, the real implementation would access database, or may be
        some abstract storage.
        :return:
        """
        resources = [
            Resource(title='Resource 1'),
            Resource(title='Resource 2'),
            Resource(title='Resource 3')
        ]
        return resources


@lru_cache
def get_resource_service() -> ResourceService:
    """
    A dependency for using a ResourceService
    :return:
    """
    return ResourceService()
