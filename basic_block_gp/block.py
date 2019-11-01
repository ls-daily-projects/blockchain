import json
from time import time


class Block():
    def __init__(self, index, transactions, proof, previous_hash):
        self.index = index
        self.timestamp = time()
        self.transactions = transactions
        self.proof = proof
        self.previous_hash = previous_hash

    def __str__(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True)
