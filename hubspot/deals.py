class Deals(object):
    BASE_URL = "deals/v1"

    def __init__(self, client):
        self._client = client

    def get_deals(self, **params):
        """
        Get all of the deals in an account.  Returns a paginated set of deals.

        In addition to the list of deals, each request will also return two values, 
        offset and hasMore. If hasMore is true, you'll need to make another request, 
        using the offset to get the next page of deal records.
        """
        endpoint = "/deal/paged"
        return self._client._get(self.BASE_URL + endpoint, params=params)

    def create_deal(self, data):
        """
        For a given account, create a deal. This is particularly useful if you're 
        integrating with a CRM or another application that has a similar notion of 
        a deal.

        Note that you can create associations between Deals and Contacts and Companies 
        much the same way you create an association between Companies and Contacts. 
        Associating your Deal with Contacts and Companies is not required (i.e. you 
        can create an orphaned deal). You can also pass any custom property value you 
        want to the deals API, so long as you've created the property first.

        The dealstage property is required when creating a deal. If the pipeline 
        property is not specified, the default pipeline is assumed. However, it is 
        recommended to always specify the pipeline, especially on accounts with multiple 
        pipelines. You can manage pipelines and dealstages through the CRM Pipelines API.
        """
        endpoint = "/deal"
        data = {"properties": [{"name": k, "value": v}
                               for k, v in data.items()]}
        return self._client._post(self.BASE_URL + endpoint, json=data)

    def delete_deal(self, deal_id):
        """
        Deletes the exisiting deal specified by :dealId.
        """
        endpoint = "/deal/{}".format(deal_id)
        return self._client._delete(self.BASE_URL + endpoint)

    def get_recently_created_deals(self, **params):
        """
        Get all deals in a account sorted by their created date, with the most 
        recently created deals first. Use the offset parameter returned in a 
        response to get the next set of deals.
        """
        endpoint = "/deal/recent/created"
        return self._client._get(self.BASE_URL + endpoint, params=params)

    def get_deal(self, deal_id, **params):
        """
        Returns an object representing the deal with the id :dealId associated 
        with the specified account.

        Two important fields will be returned to you that identify the appropriate
        associations with the deal: associatedCompanyIds returns the id of the 
        company associated with the deal, and associatedVids returns the ids of the
        contacts associated with the deal.

        You can then perform lookups on either the contacts or the company.
        """
        endpoint = "/deal/{}".format(deal_id)
        return self._client._get(self.BASE_URL + endpoint, params=params)
