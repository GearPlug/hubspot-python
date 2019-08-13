class Integrations(object):
    BASE_URL = "integrations/v1"

    def __init__(self, client):
        self._client = client

    def get_account_details(self, **params):
        endpoint = "/me"
        return self._client._get(self.BASE_URL + endpoint, params=params)

    def get_daily_api_usage(self, **params):
        endpoint = "/limit/daily"
        return self._client._get(self.BASE_URL + endpoint, params=params)
