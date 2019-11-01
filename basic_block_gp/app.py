from flask import Flask, jsonify, request

from blockchain import Blockchain

blockchain = Blockchain()

app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    return "<h1>Welcome to Blockchain!</h1>"


@app.route('/chain', methods=['GET'])
def full_chain():
    chain = [str(c) for c in blockchain.chain]

    return jsonify({
        "chain": chain,
        "length": len(chain)
    }), 200


@app.route('/mine', methods=['GET'])
def mine():
    proof = blockchain.proof_of_work()

    previous_hash = blockchain.hash(blockchain.last_block)
    new_block = blockchain.new_block(proof, previous_hash)
    blockchain.chain.append(new_block)

    return jsonify({
        "message": "New Block Forged",
        "block": str(new_block)
    }), 200


# Run the program on port 5000
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
