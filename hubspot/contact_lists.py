class ContactLists(object):
    BASE_URL = "contacts/v1"

    def __init__(self, client):
        self._client = client

    def get_contact_lists(self, **params):
        endpoint = "/lists"
        return self._client._get(self.BASE_URL + endpoint, params=params)

    def create_contact_list(self, data):
        endpoint = "/lists"
        return self._client._post(self.BASE_URL + endpoint, json=data)

    def delete_contact_list(self, contact_list_id):
        endpoint = "/lists/{0}".format(contact_list_id)
        return self._client._delete(self.BASE_URL + endpoint)

    def get_recently_added_contacts_in_a_list(self, **params):
        endpoint = "/lists/recently_updated/contacts/recent"
        return self._client._get(self.BASE_URL + endpoint, params=params)

    def get_contact_list(self, contact_list_id, **params):
        endpoint = "/lists/{0}".format(contact_list_id)
        return self._client._get(self.BASE_URL + endpoint, params=params)
