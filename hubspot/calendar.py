class Calendar(object):
    BASE_URL = "calendar/v1"

    def __init__(self, client):
        self._client = client

    def create_task(self, data):
        endpoint = "/events/task"
        return self._client._post(self.BASE_URL + endpoint, json=data)
