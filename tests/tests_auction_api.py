import unittest
import json
import requests

from auction_manager import AuctionManager


class AuctionApiTest(unittest.TestCase):
    def setUp(self):
        self.url = "http://127.0.0.1:5000"

    def tearDown(self):
        AuctionManager(load_existing_records=False)

    def test_can_get_stats(self):
        response = requests.get(self.url + "/stats")
        self.assertEqual(response.status_code, 200)

    def test_can_post_bids(self):
        new_bid = {"item_id": 111,
                   "price": 1.99,
                   "client_id": "123"}
        response = requests.post(self.url + "/bid", json=json.dumps(new_bid))
        self.assertEqual(response.status_code, 200)

    def test_error_when_posting_bid_out_of_format(self):
        incorrect_bid = {"item_id": 111,
                         "price": "b4.7a",
                         "client_id": "123"}
        response = requests.post(self.url + "/bid", json=json.dumps(incorrect_bid))
        self.assertEqual(response.status_code, 500)
