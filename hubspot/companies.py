"""
The contacts module provides functionality for working with companies in your
HubSpot account.
Documentation: https://developers.hubspot.com
"""

class Companies(object):
    def __init__(self, client):
        self._client = client
        self._base_url_companies = "companies/v2"

    def get_companies(self):
        endpoint = "/companies/"
        return self._client._get(endpoint=self._base_url_companies+endpoint)

    def create_company(self, data):
        """
        Create a new company in your HubSpot CRM
        :param data: A dictionary
        :return: A json
        """
        endpoint = "/companies/"
        if 'name' not in data:
            raise KeyError('The company must have a name')
        else:
            json = {"properties": [{"name": k, "value": v} for k, v in data.items()]}
            return self._client._post(endpoint=self._base_url_companies + endpoint, json=json)

    def delete_company(self, company_id):
        endpoint = "/companies/{0}".format(company_id)
        return self._client._delete(endpoint=self._base_url_companies+endpoint)

    def get_recently_created_companies(self, limit):
        endpoint = "/companies/recent/created"
        params = {'count': limit}
        return self._client._get(endpoint=self._base_url_companies+endpoint, params=params)

    def get_company(self, company_id):
        endpoint = "/companies/{0}".format(company_id)
        return self._client._get(endpoint=self._base_url_companies+endpoint)




