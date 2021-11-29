class Contacts(object):
    BASE_URL = "crm/v3/objects/contacts/"

    def __init__(self, client):
        self._client = client

    def get_contacts(self, **params):
        """
        For a given account, return all contacts that have been created
        in the account.

        A paginated list of contacts will be returned to you, with a
        maximum of 10 contacts per page by default.
        """
        return self._client._get(self.BASE_URL, params=params)

    def create_contact(self, data):
        """
        Create a new contact in HubSpot with a simple HTTP POST to the Contacts API.
        The contact will be created instantly inside of HubSpot, and will be assigned
        a unique ID (vid) that can be used to look up the contact inside of HubSpot later.-
        """
        data = {"properties": {k: v for k, v in data.items()}}
        return self._client._post(self.BASE_URL, json=data)

    def delete_contact(self, contact_id):
        """
        Delete an existing contact from a particular HubSpot portal.

        If a contact with the same email address interacts with the portal again
        (via a form submission for example) the contact will be added back into
        the user interface.
        """
        return self._client._delete(self.BASE_URL)

    def get_contact(self, contact_id, **params):
        """
        For a given account, return information about a single contact by its ID.
        The contact's unique ID is stored in a field called 'vid' which stands for
        'visitor ID'.

        This method will also return you much of the HubSpot lead "intelligence"
        that you may be accustomed to getting from the leads API, as properties
        in this new API. More of this intelligence will be available as time passes,
        but this call is where you can expect to find it.
        """
        return self._client._get(self.BASE_URL + str(contact_id), params=params)
