class Webhooks(object):
    BASE_URL = "webhooks/v1"

    def __init__(self, client):
        self._client = client

    def get_settings(self):
        endpoint = "/{}/settings".format(self._client.app_id)
        return self._client._get(self.BASE_URL + endpoint, params={"hapikey": self._client.hapikey})

    def update_settings(self, data):
        endpoint = "/{}/settings".format(self._client.app_id)
        return self._client._put(self.BASE_URL + endpoint, json=data, params={"hapikey": self._client.hapikey})

    def get_subscriptions(self):
        endpoint = "/{}/subscriptions".format(self._client.app_id)
        return self._client._get(self.BASE_URL + endpoint, params={"hapikey": self._client.hapikey})

    def create_subscription(self, data):
        endpoint = "/{}/subscriptions".format(self._client.app_id)
        return self._client._post(self.BASE_URL + endpoint, json=data, params={"hapikey": self._client.hapikey})

    def update_subscription(self, subscription_id, data):
        endpoint = "/{}/subscriptions/{}".format(self._client.app_id, subscription_id)
        return self._client._post(self.BASE_URL + endpoint, json=data, params={"hapikey": self._client.hapikey})

    def delete_subscription(self, subscription_id):
        endpoint = "/{}/subscriptions/{}".format(self._client.app_id, subscription_id)
        return self._client._delete(self.BASE_URL + endpoint, params={"hapikey": self._client.hapikey})
