from flask import Flask, request, jsonify

from .mt5_client import MT5Client

client: MT5Client | None = None

app = Flask(__name__)

@app.route("/api/v1/ping", methods=["GET"])
def ping():
    return jsonify({"message": "pong"})

@app.route("/api/v1/connect", methods=["POST"])
def connect():
    """Initialize connection to MetaTrader 5 terminal."""
    global client
    data = request.get_json() or {}
    login = data.get("login")
    password = data.get("password")
    server = data.get("server")
    if not (login and password and server):
        return jsonify({"error": "login, password and server are required"}), 400

    client = MT5Client(int(login), password, server)
    if not client.connect():
        return jsonify({"error": "failed to connect"}), 500
    return jsonify({"status": "connected"})


@app.route("/api/v1/account", methods=["GET"])
def account():
    """Return account information from connected terminal."""
    if not client or not client.is_connected():
        return jsonify({"error": "not connected"}), 400
    info = client.account_info()
    return jsonify(info)

@app.route("/api/v1/orders", methods=["POST"])
def place_order():
    if not client or not client.is_connected():
        return jsonify({"error": "not connected"}), 400
    payload = request.get_json() or {}
    symbol = payload.get("symbol")
    volume = payload.get("volume")
    order_type = payload.get("type")
    comment = payload.get("comment", "")
    if not (symbol and volume and order_type is not None):
        return jsonify({"error": "symbol, volume and type are required"}), 400

    try:
        result = client.send_market_order(symbol, float(volume), int(order_type), comment)
    except (ValueError, TypeError):
        return jsonify({"error": "volume and type must be valid numbers"}), 400
    return jsonify(result), 201

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
