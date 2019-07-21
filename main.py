import json

from flask import Flask, request, abort
from auction_manager import AuctionManager
app = Flask(__name__)


@app.route("/bid", methods=["POST"])
def post_bid():
    auction_manager = AuctionManager()
    bid_request = json.loads(request.get_json())
    try:
        auction_manager.insert_bid(bid_request)
    except ValueError:
        abort(500)
    return json.dumps(auction_manager.get_records(), default=str)


@app.route("/stats", methods=["GET"])
def get_stats():
    auction_manager = AuctionManager()
    records = auction_manager.get_records()
    return json.dumps(records, default=str)

if __name__ == "__main__":
    app.run()
