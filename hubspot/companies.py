class Companies(object):
    BASE_URL = "companies/v2"

    def __init__(self, client):
        self._client = client

    def get_companies(self, **params):
        endpoint = "/companies/paged"
        return self._client._get(self.BASE_URL + endpoint, params=params)

    def create_company(self, data):
        endpoint = "/companies/"
        data = {"properties": [{"name": k, "value": v}
                               for k, v in data.items()]}
        return self._client._post(self.BASE_URL + endpoint, json=data)

    def delete_company(self, company_id):
        endpoint = "/companies/{}".format(company_id)
        return self._client._delete(self.BASE_URL + endpoint)

    def get_recently_created_companies(self, **params):
        endpoint = "/companies/recent/created"
        return self._client._get(self.BASE_URL + endpoint, params=params)

    def get_company(self, company_id, **params):
        endpoint = "/companies/{}".format(company_id)
        return self._client._get(self.BASE_URL + endpoint, params=params)
