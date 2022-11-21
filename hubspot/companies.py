class Companies(object):
    BASE_URL = "crm/v3/objects/companies/"

    def __init__(self, client):
        self._client = client

    def get_companies(self, **params):
        """
        Used to get all of the companies in a account. Returns a paginated
        list of companies.

        The paging cursor token of the last successfully read resource will
        be returned as the paging.next.after JSON property of a paged response
        containing more results.
        """
        return self._client._get(self.BASE_URL, params=params)

    def create_company(self, data):
        """
        For a given account, create a company. This is particularly useful
        if you're integrating with a CRM or another application that has a
        similar notion of a company.

        This will return an object representing your newly created company.
        """
        data = {"properties": {k: v for k, v in data.items()}}
        return self._client._post(self.BASE_URL, json=data)

    def delete_company(self, company_id):
        """
        Deletes the exisiting company specified by :companyId. Returns JSON
        indicating whether or not the specified company was actually deleted.

        Since companies play a central role in the CRM, it is a best practice
        not to delete a company unless your application has created them.
        """
        return self._client._delete(self.BASE_URL + str(company_id))

    def get_company(self, company_id, **params):
        return self._client._get(self.BASE_URL + str(company_id), params=params)
