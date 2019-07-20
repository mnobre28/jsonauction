import requests
import json
import pytest

# temporary testing
def test_send_bid():
    bid_dict = {"item_id": "123",
                "price": 1.99,
                "client_id": "123"}
    response = requests.post("http://127.0.0.1:5000/bid", json=json.dumps(bid_dict))
    print("finish")

test_send_bid()
