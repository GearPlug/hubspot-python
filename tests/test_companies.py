import os
from unittest import TestCase
from hubspot.client import Client

class CompaniesTest(TestCase):
    def setUp(self):
        self.client = Client(os.environ.get('token'))

    def test_create_company(self):
        result_create = self.client.companies.create_company(data={'name':'my company'}).json()
        _id = None
        _companies = self.client.companies.get_companies().json()['companies']
        for company in _companies:
            if company['companyId'] == result_create['companyId']:
                _id = company['companyId']
        self.assertIsNotNone(_id)
        self.client.companies.delete_company(result_create['companyId'])

    def test_delete_company(self):
        result_create = self.client.companies.create_company(data={'name':'my company'}).json()
        self.client.companies.delete_company(result_create['companyId'])
        _id = None
        _companies = self.client.companies.get_companies().json()['companies']
        for company in _companies:
            if company['companyId'] == result_create['companyId']:
                _id = company['companyId']
        self.assertIsNone(_id)
