import os
from unittest import TestCase
from hubspot.client import Client

class FieldsTest(TestCase):
    def setUp(self):
        self.client = Client(os.environ.get('token'))

    def test_get_fields(self):
        _modules = ['deals', 'companies', 'contacts']
        for _module in _modules:
            result = self.client.fields.get_fields(_module).json()
            self.assertIsInstance(result, list)
            self.assertIsInstance(result[0], dict)
