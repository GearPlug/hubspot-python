class ContactLists(object):
    BASE_URL = "contacts/v1"

    def __init__(self, client):
        self._client = client

    def get_contact_lists(self, **params):
        """
        Return the contact lists for a portal.

        By default, you will get up to 20 lists to you at a time.
        You can get more lists in a single request (up to 250) using
        the count parameter. Each response will include an offset,
        which can be used with the offset= parameter in the next
        request to get the next page of lists.

        The listId is the account specific ID for the list.
        This value never changes for a particular list. The internalListId
        is an internal identifier used to track the list criteria revisions,
         and is subject to change when the list is modified.

        See the Contact List Overview for details about the returned data
        """
        endpoint = "/lists"
        return self._client._get(self.BASE_URL + endpoint, params=params)

    def create_contact_list(self, data):
        """
        Create a new list in a given HubSpot account to populate with contacts.

        Creating this list show in the user interface, so beware that users
        will be able to edit and even delete lists that are programatically
        created in HubSpot.
        """
        endpoint = "/lists"
        return self._client._post(self.BASE_URL + endpoint, json=data)

    def delete_contact_list(self, contact_list_id):
        """
        Delete a list in a given HubSpot account, identified by its unique ID.

        Note that lists can be used by users to trigger marketing automation
        campaigns, so a good best practice is to only delete the lists that
        your integration with HubSpot has created.
        """
        endpoint = "/lists/{}".format(contact_list_id)
        return self._client._delete(self.BASE_URL + endpoint)

    def get_recently_added_contacts_in_a_list(self, **params):
        """
        For a given HubID and a given list, return contacts that have been
        recently added to that list, starting with the most recently added
        contact and pageing backwards. A paginated list of contacts will be
        returned to you, with a maximum of 100 contacts per page, as specified
        by the "count" parameter.
        """
        endpoint = "/lists/recently_updated/contacts/recent"
        return self._client._get(self.BASE_URL + endpoint, params=params)

    def get_contact_list(self, contact_list_id, **params):
        """
        For a given portal, return a contact list by its unique ID. This returns
         only the metadata for the list; see this page for getting the contact
         records in the list.

        If you are not storing the list ids inside of your application, you'll
        need to first find the list id by using the get all lists endpoint.

        See the Contact List Overview for details about the returned data
        """
        endpoint = "/lists/{}".format(contact_list_id)
        return self._client._get(self.BASE_URL + endpoint, params=params)

    def add_contact_to_list(self, contact_list_id, data):
        """
        Add contact records that have already been created in the system to
        a contact list. You can add multiple records at once, either by vid
        or by email address. Up to 500 records can be added to a list in a
        single request, including records specified by ID and by email.

        Please note that you cannot manually add contacts to dynamic lists.
        To determine whether a list is dynamic or static, when you get a list,
        you will see a flag called dynamic that equates to true or fals
        """
        endpoint = "/lists/{}/add".format(contact_list_id)
        return self._client._post(self.BASE_URL + endpoint, json=data)
