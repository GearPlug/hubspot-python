class Integrations(object):
    BASE_URL = "integrations/v1"

    def __init__(self, client):
        self._client = client

    def get_account_details(self, **params):
        """
        Get the details for a HubSpot account, based on the provided API key or
        access token.

        Currently, this will include the Portal ID (often called the Hub ID) of
        the account, the time zone setting of the account, and the selected currency
        of the account.
        """
        endpoint = "/me"
        return self._client._get(self.BASE_URL + endpoint, params=params)

    def get_daily_api_usage(self, **params):
        """
        Check to see how many API calls that have been made for a portal for
        the current day, as well as the time that the limit will reset.
        The current day is measured from midnight to midnight based on the
        time zone setting of the portal.

        See the API Usage Guidelines for more details about HubSpot's API
        limits, and this page for details about working with those limits.

        The data returned returned by this endpoint will be cached for 5 minutes.
        Check the fetchStatus and collectedAt fields in the response to determine
        if the response was from cache.
        """
        endpoint = "/limit/daily"
        return self._client._get(self.BASE_URL + endpoint, params=params)
