"""
The deals module provides fieds from different modules in your HubSpot account.
Documentation: https://developers.hubspot.com
"""

from hubspot import exception

class Fields(object):
    def __init__(self, client):
        self._client = client
        self._base_url_fields = "properties/v1/module/properties"

    def get_fields(self, module):
        """
        Get fields from a module
        :param module: String name of the module only the modules "contacts, companies, deals are allowed"
        :return: a Json
        """
        if module in ['deals', 'companies', 'contacts']:
            return self._client._get(endpoint=self._base_url_fields.replace("module", module))
        else:
            raise exception.ModuleNotFound('Your must provide "deals", "companies", "contacts" such a module')