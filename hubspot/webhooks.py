class Webhooks(object):
    BASE_URL = "webhooks/v1"

    def __init__(self, client):
        self._client = client

    def get_subscriptions(self):
        endpoint = "/{}/subscriptions".format(self._client.app_id)
        return self._client._get(self.BASE_URL + endpoint)

    def create_subscription(self, data):
        endpoint = "/{}/subscriptions".format(self._client.app_id)
        return self._client._post(self.BASE_URL + endpoint, json=data)

    def update_subscription(self, subscription_id, data):
        endpoint = "/{}/subscriptions/{}".format(
            self._client.app_id, subscription_id)
        return self._client._post(self.BASE_URL + endpoint, json=data)

    def delete_subscription(self, subscription_id):
        endpoint = "/{}/subscriptions/{}".format(
            self._client.app_id, subscription_id)
        return self._client._delete(self.BASE_URL + endpoint)
