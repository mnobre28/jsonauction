import unittest
import os
from datetime import datetime, timedelta

from auction_manager import AuctionManager


class AuctionManagerTest(unittest.TestCase):
    def setUp(self):
        self.first_bid = {"item_id": 111,
                          "price": 1.99,
                          "client_id": "123"}
        self.second_bid = {"item_id": 222,
                           "price": 3.23,
                           "client_id": "456"}
        self.highest_bid = {"item_id": 111,
                            "price": 5.23,
                            "client_id": "456"}

    def tearDown(self):
        os.remove('files/records.json')

    def test_can_insert_bids(self):
        self.auction_manager = AuctionManager(load_existing_records=False)
        self.auction_manager.insert_bid(self.first_bid)
        self.assertEqual(self.auction_manager.get_total_bids(), 1)
        self.assertEqual(self.auction_manager.get_total_hits(), 1)
        registered_bid = self.auction_manager.get_bid_with_registered_item_id(self.first_bid["item_id"])
        self.assertEqual(registered_bid["best_bid"]["client_id"], self.first_bid["client_id"])
        self.assertEqual(registered_bid["best_bid"]["price"], self.first_bid["price"])
        timestamp_difference = datetime.now() - registered_bid["best_bid"]["timestamp"]
        self.assertLessEqual(timestamp_difference, timedelta(seconds=1))

        self.auction_manager.insert_bid(self.second_bid)
        self.assertEqual(self.auction_manager.get_total_bids(), 2)
        self.assertEqual(self.auction_manager.get_total_hits(), 2)
        registered_bid = self.auction_manager.get_bid_with_registered_item_id(self.second_bid["item_id"])
        self.assertEqual(registered_bid["best_bid"]["client_id"], self.second_bid["client_id"])
        self.assertEqual(registered_bid["best_bid"]["price"], self.second_bid["price"])
        timestamp_difference = datetime.now() - registered_bid["best_bid"]["timestamp"]
        self.assertLessEqual(timestamp_difference, timedelta(seconds=1))

    def test_can_update_bids(self):
        self.auction_manager = AuctionManager(load_existing_records=False)
        self.auction_manager.insert_bid(self.first_bid)
        self.auction_manager.insert_bid(self.highest_bid)
        self.assertEqual(self.auction_manager.get_total_bids(), 1)
        self.assertEqual(self.auction_manager.get_total_hits(), 2)
        registered_bid = self.auction_manager.get_bid_with_registered_item_id(self.highest_bid["item_id"])
        self.assertEqual(registered_bid["best_bid"]["client_id"], self.highest_bid["client_id"])
        self.assertEqual(registered_bid["best_bid"]["price"], self.highest_bid["price"])
        timestamp_difference = datetime.now() - registered_bid["best_bid"]["timestamp"]
        self.assertLessEqual(timestamp_difference, timedelta(seconds=1))

    def test_can_correctly_increment_number_of_hits_and_bids(self):
        self.auction_manager = AuctionManager(load_existing_records=False)
        self.auction_manager.insert_bid(self.first_bid)
        self.auction_manager.insert_bid(self.second_bid)
        self.auction_manager.insert_bid(self.highest_bid)
        self.assertEqual(self.auction_manager.get_total_bids(), 2)
        self.assertEqual(self.auction_manager.get_total_hits(), 3)

    def test_cannot_accept_out_of_format_bids(self):
        self.auction_manager = AuctionManager(load_existing_records=False)
        first_invalid_bid = {"item_id": 45234,
                             "price": "23.a4",
                             "client_id": "123"}
        second_invalid_bid = {"item_id": 45234,
                              "price": "12few9",
                              "client_id": "123"}
        with self.assertRaises(ValueError):
            self.auction_manager.insert_bid(first_invalid_bid)
        with self.assertRaises(ValueError):
            self.auction_manager.insert_bid(second_invalid_bid)

suite = unittest.TestLoader().loadTestsFromTestCase(AuctionManagerTest)
unittest.TextTestRunner(verbosity=2).run(suite)

# def test_send_bid():
#     bid_dict = {"item_id": "123",
#                 "price": 1.99,
#                 "client_id": "123"}
#     response = requests.post("http://127.0.0.1:5000/bid", json=json.dumps(bid_dict))
#     print(response.content)
#     print("finish")