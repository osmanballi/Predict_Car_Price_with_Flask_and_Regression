import pickle
import numpy as np
from flask import Flask, request, render_template

app = Flask(__name__)
model = pickle.load(open("car.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict",methods=["POST"])
def predict():
    features = [int(x) for x in request.form.values()]
    final_features = [np.array(features)]
    prediction = model.predict(final_features)
    output = int(prediction[0])
    return render_template("index.html",prediction_text="Car price should be $ {}".format(output))
if __name__ == "__main__":
    app.run(port=5000,debug=True)