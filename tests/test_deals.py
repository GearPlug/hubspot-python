import os
from unittest import TestCase
from hubspot.client import Client
import time

class DealsTest(TestCase):
    def setUp(self):
        self.client = Client(os.environ.get('token'))

    def test_create_deal(self):
        result_create = self.client.deals.create_deal(data={'dealname':'mydealtest'}).json()
        _id = None
        _deals = self.client.deals.get_deals(30).json()['deals']
        for _deal in _deals:
            if _deal['dealId'] == result_create['dealId']:
                _id = _deal['dealId']
        self.assertIsNotNone(_id)
        self.client.deals.delete_deal(result_create['dealId'])

    def test_delete_deal(self):
        result_create = self.client.deals.create_deal(data={'dealname':'mydealtest'}).json()
        self.client.deals.delete_deal(result_create['dealId'])
        _id = None
        _deals = self.client.deals.get_deals(30).json()['deals']
        for _deal in _deals:
            if _deal['dealId'] == result_create['dealId']:
                _id = _deal['dealId']
        self.assertIsNone(_id)

    def test_get_recently_created_contacts(self):
        result_create = self.client.deals.create_deal(data={'dealname': 'mydealtest'}).json()
        _id = None
        time.sleep(10)
        _deal = self.client.deals.get_recently_created_deals(1).json()
        if _deal['results'][0]['dealId'] == result_create['dealId']:
            _id = _deal['results'][0]['dealId']
        self.assertIsNotNone(_id)
        self.client.deals.delete_deal(result_create['dealId'])

    def test_get_deal(self):
        result_create = self.client.deals.create_deal(data={'dealname': 'mydealtest'}).json()
        try:
            self.client.deals.get_deal(result_create['dealId'])
            find = True
        except:
            find = False
        self.assertTrue(find)
        self.client.deals.delete_deal(result_create['dealId'])