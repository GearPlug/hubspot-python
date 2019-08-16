class Calendar(object):
    BASE_URL = "calendar/v1"

    def __init__(self, client):
        self._client = client

    def create_task(self, data):
        """
        Create a new task for Calendar. Creating a task of type BLOG_POST, EMAIL, 
        or LANDING_PAGE will create a draft of the respective content and associate 
        it with the task, returning a contentId in the response.

        When specifying an owner, use the Owners API to get a list of owner Ids.
        """
        endpoint = "/events/task"
        return self._client._post(self.BASE_URL + endpoint, json=data)
