from flask import Flask, request, jsonify
from model import predict_sentiment

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Welcome to the Sentiment Analysis Service - CI/CD update!"}), 200

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json() or {}
    text = data.get("text", "")

    if not text:
        return jsonify({"error": "Missing 'text' field"}), 400

    prediction = predict_sentiment(text)
    return jsonify({"input": text, "prediction": prediction}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
