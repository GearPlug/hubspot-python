class Deals(object):
    BASE_URL = "deals/v1"

    def __init__(self, client):
        self._client = client

    def get_deals(self, **params):
        endpoint = "/deal/paged"
        return self._client._get(self.BASE_URL + endpoint, params=params)

    def create_deal(self, data):
        endpoint = "/deal"
        data = {"properties": [{"name": k, "value": v}
                               for k, v in data.items()]}
        return self._client._post(self.BASE_URL + endpoint, json=data)

    def delete_deal(self, deal_id):
        endpoint = "/deal/{0}".format(deal_id)
        return self._client._delete(self.BASE_URL + endpoint)

    def get_recently_created_deals(self, **params):
        endpoint = "/deal/recent/created"
        return self._client._get(self.BASE_URL + endpoint, params=params)

    def get_deal(self, deal_id, **params):
        endpoint = "/deal/{0}".format(deal_id)
        return self._client._get(self.BASE_URL + endpoint, params=params)
