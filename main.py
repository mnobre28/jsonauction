from flask import Flask, request
app = Flask(__name__)


@app.route("/bid", methods=["POST"])
def post_bid():
    bid_request = request.get_json()
    # if item_id doesnt exist, add to list.
    # if item_id exists, increment counter.
    # client_id has no validation
    # item_id must be alphanumeric, price must be float, client_id must be alphanumeric
    return "bid posted"


@app.route("/stats")
def get_stats():
    return "get stats"

if __name__ == "__main__":
    app.run()
