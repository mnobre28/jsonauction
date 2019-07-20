import json
import os

#CURRENT_DIR = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))


class StatsManager(object):
    def __init__(self):
        self.stats_file = None
        # self.file_path = os.path.join(CURRENT_DIR, "files\\stats.json")
        self._create_new_file()

    def get_or_create_stats_file(self):
        raise NotImplementedError

    def _create_new_file(self):
        default_data = {"total_bids": 0,
                        "total_hits": 0,
                        "bids": []}
        # with open(self.file_path, 'w') as f:
            # json.dump(default_data, f)
        self.stats_file = default_data

    def insert_bid(self, new_bid):
        raise NotImplementedError

    def _insert_new_bid(self, new_bid):
        raise NotImplementedError

    def _update_existing_bid(self, new_bid):
        raise NotImplementedError

    def _save_file(self):
        raise NotImplementedError
