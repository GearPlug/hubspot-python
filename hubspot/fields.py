from hubspot import exception


class Fields(object):
    BASE_URL = "properties/v1/{}/properties"

    def __init__(self, client):
        self._client = client

    def get_fields(self, module):
        if module in ['deals', 'companies', 'contacts']:
            return self._client._get(self.BASE_URL.format(module))

        raise exception.ModuleNotFound(
            'Your must provide "deals", "companies", "contacts" such a module')
