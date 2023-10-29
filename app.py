from flask import Flask, jsonify, request, templating, send_file
from ml_model import Predictions

app = Flask(__name__)
prediction = Predictions()


@app.route("/", methods=["GET"])
def index():
    return templating.render_template("index.html")


@app.route("/", methods=["POST"])
def api_predict():
    image_url = request.form.get("image_url")
    prediction_result = prediction.start(image_url=image_url)
    data = {"image_url": image_url, "prediction": prediction_result}
    return templating.render_template("index.html", data=data)


if __name__ == "__main__":
    app.run(debug=True, port=1200)


# print(model.predict("your_image.jpg").json())
# model.predict("your_image.jpg").save("prediction.jpg")
