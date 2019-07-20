import unittest
import requests
import json
import pytest
from datetime import datetime, timedelta

# temporary testing
from auction_manager import AuctionManager


# def test_send_bid():
#     bid_dict = {"item_id": "123",
#                 "price": 1.99,
#                 "client_id": "123"}
#     response = requests.post("http://127.0.0.1:5000/bid", json=json.dumps(bid_dict))
#     print("finish")
#
# test_send_bid()


class AuctionManagerTest(unittest.TestCase):
    def setUp(self):
        self.auction_manager = AuctionManager()

    def test_can_insert_bids(self):
        first_bid = {"item_id": 111,
                     "price": 1.99,
                     "client_id": "123"}
        self.auction_manager.insert_bid(first_bid)
        self.assertEqual(self.auction_manager.get_total_bids(), 1)
        self.assertEqual(self.auction_manager.get_total_hits(), 1)
        registered_bid = self.auction_manager.get_bid_with_registered_item_id(first_bid["item_id"])
        self.assertEqual(registered_bid["best_bid"]["client_id"], first_bid["client_id"])
        self.assertEqual(registered_bid["best_bid"]["price"], first_bid["price"])
        timestamp_difference = datetime.now() - registered_bid["best_bid"]["timestamp"]
        self.assertLessEqual(timestamp_difference, timedelta(seconds=1))

        second_bid = {"item_id": 222,
                      "price": 3.23,
                      "client_id": "456"}
        self.auction_manager.insert_bid(second_bid)
        self.assertEqual(self.auction_manager.get_total_bids(), 2)
        self.assertEqual(self.auction_manager.get_total_hits(), 2)
        registered_bid = self.auction_manager.get_bid_with_registered_item_id(second_bid["item_id"])
        self.assertEqual(registered_bid["best_bid"]["client_id"], second_bid["client_id"])
        self.assertEqual(registered_bid["best_bid"]["price"], second_bid["price"])
        timestamp_difference = datetime.now() - registered_bid["best_bid"]["timestamp"]
        self.assertLessEqual(timestamp_difference, timedelta(seconds=1))

suite = unittest.TestLoader().loadTestsFromTestCase(AuctionManagerTest)
unittest.TextTestRunner(verbosity=2).run(suite)
