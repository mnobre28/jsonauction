import json
import os
from datetime import datetime

CURRENT_DIR = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
RECORDS_PATH = os.path.join(CURRENT_DIR, "files\\records.json")


class AuctionManager(object):
    def __init__(self, load_existing_records=True):
        self.records = self._get_or_create_files(load_existing_records)

    def get_records(self):
        return self.records

    def _get_or_create_files(self, load_existing_records):
        if os.path.isfile(RECORDS_PATH) and load_existing_records:
            return self._load_existing_file()
        return self._create_new_file()

    @staticmethod
    def _load_existing_file():
        with open(RECORDS_PATH, 'r') as f:
            return json.load(f)

    @staticmethod
    def _create_new_file():
        default_file = {"total_bids": 0,
                        "total_hits": 0,
                        "bids": []}
        with open(RECORDS_PATH, 'w') as f:
            json.dump(default_file, f)
        return default_file

    def _save_records(self):
        with open(RECORDS_PATH, 'w') as f:
            json.dump(self.records, f, default=str)

    def insert_bid(self, new_bid):
        if not self.is_bid_valid(new_bid):
            raise ValueError("Price must be a float value.")
        self.records["total_hits"] = self.records["total_hits"] + 1
        bid_to_update = self.get_bid_with_registered_item_id(new_bid["item_id"])
        if bid_to_update is None:
            self._create_new_bid(new_bid)
            self.records["total_bids"] = self.records["total_bids"] + 1
        else:
            self._update_bid(bid_to_update, new_bid)
        self._save_records()

    def get_total_hits(self):
        return self.records.get("total_hits")

    def get_total_bids(self):
        return self.records.get("total_bids")

    def get_bid_with_registered_item_id(self, item_id):
        for bid in self.records["bids"]:
            if item_id == bid["item_id"]:
                return bid
        return None

    @staticmethod
    def is_bid_valid(bid):
        try:
            if float(bid["price"]):
                return True
        except ValueError:
            return False

    def _update_bid(self, bid_to_update, new_bid):
        bid_to_update["hits"] = bid_to_update["hits"] + 1
        if new_bid["price"] > bid_to_update["best_bid"]["price"]:
            bid_to_update["best_bid"] = self._format_bid_as_best_bid(new_bid)

    def _create_new_bid(self, best_bid):
        new_bid = {"item_id": best_bid["item_id"],
                   "hits": 1,
                   "best_bid": self._format_bid_as_best_bid(best_bid)}
        self.records["bids"].append(new_bid)

    @staticmethod
    def _format_bid_as_best_bid(bid):
        return {"client_id": bid["client_id"],
                "price": bid["price"],
                "timestamp": datetime.now()}

