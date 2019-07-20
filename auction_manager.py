import json
import os
from datetime import datetime

#CURRENT_DIR = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))


class AuctionManager(object):
    def __init__(self):
        self.records = None
        # self.file_path = os.path.join(CURRENT_DIR, "files\\stats.json")
        self._create_new_file()

    def get_records(self):
        return self.records

    def get_or_create_stats_file(self):
        return self.records

    def _create_new_file(self):
        default_data = {"total_bids": 0,
                        "total_hits": 0,
                        "bids": []}
        # with open(self.file_path, 'w') as f:
            # json.dump(default_data, f)
        self.records = default_data

    def insert_bid(self, new_bid):
        self.records["total_hits"] = self.records["total_hits"] + 1
        bid_to_update = self.get_bid_with_registered_item_id(new_bid["item_id"])
        if bid_to_update is None:
            self._create_new_bid(new_bid)
            self.records["total_bids"] = self.records["total_bids"] + 1
        else:
            self._update_bid(bid_to_update, new_bid)

    def get_total_hits(self):
        return self.records.get("total_hits")

    def get_total_bids(self):
        return self.records.get("total_bids")

    def get_bid_with_registered_item_id(self, item_id):
        for bid in self.records["bids"]:
            if item_id == bid["item_id"]:
                return bid
        return None

    def _update_bid(self, bid_to_update, new_bid):
        bid_to_update["hits"] = bid_to_update["hits"] + 1
        if new_bid["best_bid"]["price"] > bid_to_update["best_bid"]["price"]:
            bid_to_update["best_bid"] = self._format_as_best_bid(new_bid)

    def _create_new_bid(self, best_bid):
        new_bid = {"item_id": best_bid["item_id"],
                   "hits": 1,
                   "best_bid": self._format_as_best_bid(best_bid)}
        self.records["bids"].append(new_bid)

    @staticmethod
    def _format_as_best_bid(bid):
        return {"client_id": bid["client_id"],
                "price": bid["price"],
                "timestamp": datetime.now()}

