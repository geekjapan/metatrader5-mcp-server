from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/api/v1/ping", methods=["GET"])
def ping():
    return jsonify({"message": "pong"})

@app.route("/api/v1/orders", methods=["POST"])
def place_order():
    payload = request.get_json() or {}
    # TODO: implement order placement logic
    return jsonify({"received": payload}), 201

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
