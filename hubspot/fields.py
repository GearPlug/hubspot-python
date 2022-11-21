from hubspot import exceptions


class Fields(object):
    BASE_URL = "crm/v3/properties/{}"

    def __init__(self, client):
        self._client = client

    def get_fields(self, module):
        if module in ["deals", "companies", "contacts"]:
            return self._client._get(self.BASE_URL.format(module))

        raise exceptions.ModuleNotFoundError('Your must provide "deals", "companies", "contacts" such a module')
