import hashlib
import json
from time import time
from uuid import uuid4

from block import Block


class Blockchain():
    def __init__(self, difficulty=3):
        self.chain = []
        self.current_transactions = []
        self.difficulty = difficulty

        # Create the genesis block
        genesis_block = self.new_block(proof=100, previous_hash=1)
        self.chain.append(genesis_block)

    def new_block(self, proof, previous_hash=None):
        """
        Create a new Block in the Blockchain
        """
        new_index = len(self.chain) + 1

        if not previous_hash:
            previous_hash = self.hash(self.last_block)

        block = Block(new_index, self.current_transactions,
                      proof, previous_hash)

        # Why are we resetting the current transactions?
        # What are current transactions even for?
        self.current_transactions = []

        return block

    @staticmethod
    def hash(block):
        """
        Creates a SHA-256 hash of a Block
        """
        encoded_block_string = str(block).encode()
        hex_hash = hashlib.sha256(encoded_block_string).hexdigest()
        return hex_hash

    @property
    def last_block(self):
        return self.chain[-1]

    def proof_of_work(self):
        """
        Simple Proof of Work Algorithm
        """
        encoded_block_string = str(self.last_block).encode()
        proof = 0

        while not self.valid_proof(encoded_block_string, proof):
            proof += 1

        return proof

    def valid_proof(self, block_string, proof):
        """
        Validates the Proof:  Does hash(block_string, proof) contain 3
        leading zeroes?  Return true if the proof is valid
        :param block_string: <string> The stringified block to use to
        check in combination with `proof`
        :param proof: <int?> The value that when combined with the
        stringified previous block results in a hash that has the
        correct number of leading zeroes.
        :return: True if the resulting hash is a valid proof, False otherwise
        """
        guess = block_string + f"{proof}".encode()
        guess_hex_hash = hashlib.sha256(guess).hexdigest()
        guess_leading_zeroes = guess_hex_hash[:self.difficulty]
        expected_leading_zeroes = "0"*self.difficulty
        is_valid = guess_leading_zeroes == expected_leading_zeroes
        if is_valid:
            print(guess_hex_hash)
        return is_valid


node_identifier = str(uuid4()).replace('-', '')
