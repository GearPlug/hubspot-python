class Contacts(object):
    BASE_URL = "contacts/v1"

    def __init__(self, client):
        self._client = client

    def get_contacts(self, **params):
        endpoint = "/lists/all/contacts/all"
        return self._client._get(self.BASE_URL + endpoint, params=params)

    def create_contact(self, data):
        endpoint = "/contact"
        data = {"properties": [{"property": k, "value": v}
                               for k, v in data.items()]}
        return self._client._post(self.BASE_URL + endpoint, json=data)

    def delete_contact(self, contact_id):
        endpoint = "/contact/vid/{}".format(contact_id)
        return self._client._delete(self.BASE_URL + endpoint)

    def get_recently_created_contacts(self, **params):
        endpoint = "/lists/all/contacts/recent"
        return self._client._get(self.BASE_URL + endpoint, params=params)

    def get_contact(self, contact_id, **params):
        endpoint = "/contact/vid/{}/profile".format(contact_id)
        return self._client._get(self.BASE_URL + endpoint, params=params)
