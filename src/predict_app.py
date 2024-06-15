import os

from dotenv import dotenv_values
from flask import Flask, request, send_from_directory
from flask_cors import CORS
from flask_httpauth import HTTPTokenAuth
from joblib import load
from utils import predict_cpu_bounded, predict_cpu_multithread, predict_io_bounded

MODEL_SAVE_PATH = "models/linear_regression_v01.joblib"

app = Flask(__name__)
CORS(app)

config = dotenv_values(".env")
auth = HTTPTokenAuth(scheme="Bearer")

tokens = {
    config["APP_TOKEN"]: "user1",
}

model = load(MODEL_SAVE_PATH)


@auth.verify_token
def verify_token(token):
    if token in tokens:
        return tokens[token]


def predict(in_data: dict) -> int:
    """Predict house price from input data parameters.
    :param in_data: house parameters.
    :raise Error: If something goes wrong.
    :return: House price, RUB.
    :rtype: int
    """
    # data = request.get_json()
    # area = data.get("area")
    # mode = data.get("mode")
    # n = data.get("n", 5_000_000)

    # if mode == "io":
    #     result = predict_io_bounded(area)
    # elif mode == "cpu":
    #     result = predict_cpu_bounded(area, n)
    # elif mode == "multithread":
    #     result = predict_cpu_multithread(area, n)
    area = float(in_data["area"])
    price = model.predict([[area]])
    return int(price)
    # return int(result)


@app.route("/favicon.ico")
def favicon():
    return send_from_directory(
        os.path.join(app.root_path, "static"),
        "favicon.ico",
        mimetype="image/vnd.microsoft.icon",
    )


@app.route("/")
def home():
    return """
    <html>
    <head>
    <link rel="shortcut icon" href="/favicon.ico">
    </head>
    <body>
    <h1>Housing price service.</h1> Use /predict endpoint
    </body>
    </html>
    """


@app.route("/predict", methods=["POST"])
@auth.login_required
def predict_web_serve():
    """Dummy service"""
    in_data = request.get_json()
    price = predict(in_data)
    return {"price": price}


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
