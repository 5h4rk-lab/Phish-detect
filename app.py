from flask import Flask, render_template, request, jsonify
from phishing_utils import extract_features, is_valid_url
from model import train_model, evaluate_model, load_data, preprocess_data
from sklearn.model_selection import train_test_split

import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        url = request.form["url"]
        features = extract_features(url)
        prediction = model.predict([features])[0]
        return render_template("index.html", prediction=prediction)
    return render_template("index.html")

@app.route("/api/check_url", methods=["POST"])
def check_url():
    data = request.get_json()
    if "url" not in data:
        return jsonify({"error": "Missing URL in request data"}), 400

    url = data["url"]

    if not is_valid_url(url):
        return jsonify({"error": "Invalid URL"}), 400

    features = extract_features(url)
    prediction = model.predict([features])[0]
    return jsonify({"url": url, "is_phishing": bool(prediction)})

if __name__ == "__main__":
    # Load and preprocess data
    data_path = os.path.join("phishing_site_urls.csv")
    data = load_data(data_path)
    X, y = preprocess_data(data)

    # Train and evaluate model
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = train_model(X_train, y_train)
    accuracy = evaluate_model(model, X_test, y_test)
    print("Model accuracy:", accuracy)

    app.run(debug=True)
