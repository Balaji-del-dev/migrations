from flask import Flask, jsonify, request

app = Flask(__name__)

# Root route
@app.route("/")
def index():
    return jsonify({"message": "Hello, world!"})

# Example GET route
@app.route("/status")
def status():
    return jsonify({"status": "ok", "message": "Server is running"})

# Example dynamic route
@app.route("/greet/<name>")
def greet(name):
    return jsonify({"message": f"Hello, {name}!"})

# Example POST route
@app.route("/echo", methods=["POST"])
def echo():
    data = request.get_json()
    return jsonify({"you_sent": data})

# Example math API
@app.route("/add", methods=["GET"])
def add():
    # Get query params ?a=3&b=5
    a = request.args.get("a", type=int)
    b = request.args.get("b", type=int)
    if a is None or b is None:
        return jsonify({"error": "Please provide both 'a' and 'b' as query parameters"}), 400
    return jsonify({"result": a + b})

if __name__ == "__main__":
    app.run(debug=True)
