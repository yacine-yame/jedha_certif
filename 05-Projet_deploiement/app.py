
from flask import Flask, request, jsonify, render_template
import joblib
import pathlib

app = Flask(__name__)


# get relative data folder
# PATH = pathlib.Path(__file__).parent
# DATA_PATH = PATH.joinpath("../models").resolve()
# model = joblib.load(DATA_PATH.joinpath("model.joblib"))


MODEL_PATH = "models/model.joblib"

@app.route("/predict", methods=["POST"])
def predict():
    # Check parameters
    if request.json:
        # Get JSON as dictionnary
        json_input = request.get_json()
        # Load model
        model = joblib.load(MODEL_PATH)
        # Make prediction (the model expects a 2D array that is why we put year
        # in a list of list) and return it
        prediction = model.predict(json_input["input"])
        prediction = prediction = str(prediction[0])
        # Return prediction
        return jsonify({"predict": prediction}), 200
    return jsonify({"msg": "Error, no JSON detected"})

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)
    # app.run(port=8000,debug=True)
    #app.run(host='0.0.0.0',port=8000,debug=True)