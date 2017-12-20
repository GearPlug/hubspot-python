"""
The contacts module provides functionality for working with contacts in your
HubSpot account.
Documentation: https://developers.hubspot.com
"""

class Contacts(object):
    def __init__(self, client):
        self._client = client
        self._base_url_contacts = "contacts/v1"

    def get_contacts(self):
        endpoint = "/lists/all/contacts/all"
        return self._client._get(endpoint=self._base_url_contacts+endpoint)

    def create_contact(self, data):
        """
        Create a new contact in your HubSpot CRM
        :param data: A dictionary
        :return: A json
        """
        endpoint = "/contact"
        if 'email' not in data:
            raise KeyError('The contact must have a email')
        else:
            json ={"properties": [{"property": k, "value": v} for k,v in data.items()]}
            return self._client._post(endpoint=self._base_url_contacts+endpoint, json=json)

    def delete_contact(self, contact_id):
        endpoint = "/contact/vid/{0}".format(contact_id)
        return self._client._delete(endpoint=self._base_url_contacts+endpoint)

    def get_recently_created_contacts(self, limit):
        endpoint = "/lists/all/contacts/recent"
        params = {'count': limit}
        return self._client._get(endpoint=self._base_url_contacts+endpoint, params=params)

    def get_contact(self, contact_id):
        endpoint = "/contact/vid/{0}/profile".format(contact_id)
        return self._client._get(endpoint=self._base_url_contacts + endpoint)
