import json

from flask import Flask, request
from auction_manager import AuctionManager
app = Flask(__name__)

auction_manager = AuctionManager()


@app.route("/bid", methods=["POST"])
def post_bid():
    # {"item_id": 123,
    # "price": 1.99,
    # "client_id": "123"}
    bid_request = request.get_json()
    # if item_id doesnt exist, add to list.
    # if item_id exists, increment counter.
    # client_id has no validation
    # item_id must be alphanumeric, price must be float, client_id must be alphanumeric
    return "bid posted"


@app.route("/stats", methods=["GET"])
def get_stats():
    records = auction_manager.get_records()
    return json.loads(records)

if __name__ == "__main__":
    app.run()
