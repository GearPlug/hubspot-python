"""
The deals module provides functionality for working with companies in your
HubSpot account.
Documentation: https://developers.hubspot.com
"""

class Deals(object):
    def __init__(self, client):
        self._client = client
        self._base_url_deals = "deals/v1"

    def get_deals(self, limit):
        params = {
            'includeAssociations': 'true',
            'limit': limit,
            'properties': 'dealname'
        }
        endpoint = "/deal/paged"
        return self._client._get(endpoint=self._base_url_deals+endpoint, params=params)

    def create_deal(self, data):
        """
        Create a new deal in your HubSpot CRM
        :param data: A dictionary
        :return: A json
        """
        endpoint = "/deal"
        if 'dealname' not in data:
            raise KeyError('The company must have a dealname')
        else:
            json = {"properties": [{"name": k, "value": v} for k, v in data.items()]}
            return self._client._post(endpoint=self._base_url_deals + endpoint, json=json)

    def delete_deal(self, deal_id):
        endpoint = "/deal/{0}".format(deal_id)
        return self._client._delete(endpoint=self._base_url_deals+endpoint)

    def get_recently_created_deals(self, limit):
        endpoint = "/deal/recent/created"
        params = {'count': limit}
        return self._client._get(endpoint=self._base_url_deals+endpoint, params=params)

    def get_deal(self, deal_id):
        endpoint = "/deal/{0}".format(deal_id)
        return self._client._get(endpoint=self._base_url_deals+endpoint)