class Companies(object):
    BASE_URL = "companies/v2"

    def __init__(self, client):
        self._client = client

    def get_companies(self, **params):
        """
        Used to get all of the companies in a account. Returns a paginated 
        list of companies.

        In addition to the list of companies, each request will also return 
        two values, offset and has-more. If has-more is true, you'll need 
        to make another request, using the offset to get the next page of 
        company records.
        """
        endpoint = "/companies/paged"
        return self._client._get(self.BASE_URL + endpoint, params=params)

    def create_company(self, data):
        """
        For a given account, create a company. This is particularly useful 
        if you're integrating with a CRM or another application that has a 
        similar notion of a company.

        This will return an object representing your newly created company.
        """
        endpoint = "/companies/"
        data = {"properties": [{"name": k, "value": v}
                               for k, v in data.items()]}
        return self._client._post(self.BASE_URL + endpoint, json=data)

    def delete_company(self, company_id):
        """
        Deletes the exisiting company specified by :companyId. Returns JSON 
        indicating whether or not the specified company was actually deleted.

        Since companies play a central role in the CRM, it is a best practice 
        not to delete a company unless your application has created them.
        """
        endpoint = "/companies/{}".format(company_id)
        return self._client._delete(self.BASE_URL + endpoint)

    def get_recently_created_companies(self, **params):
        """
        Returns a list of all companies sorted by the date the companies were 
        created. This is particularly useful for ongoing syncs with HubSpot 
        in which changes to companies must be captured in another system.
        """
        endpoint = "/companies/recent/created"
        return self._client._get(self.BASE_URL + endpoint, params=params)

    def get_company(self, company_id, **params):
        endpoint = "/companies/{}".format(company_id)
        return self._client._get(self.BASE_URL + endpoint, params=params)
