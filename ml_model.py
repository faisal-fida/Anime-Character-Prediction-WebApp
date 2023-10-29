from roboflow import Roboflow
from dotenv import load_dotenv
import logging
import os

# set up logging
logging.basicConfig(level=logging.INFO, format="%(name)s - %(levelname)s - %(message)s")

# load environment variables from .env
load_dotenv()
roboflow_api = os.getenv("ROBOFLOW_API_KEY")
roboflow_project = os.getenv("ROBOFLOW_PROJECT_NAME")

rf = Roboflow(api_key=roboflow_api)
project = rf.workspace().project(roboflow_project)
model = project.version(3).model

# instantiate the Roboflow API
class Predictions:
    def __init__(self):
        pass

    def predict(self, image_url: str, hosted: bool=False):
        prediction = model.predict(image_url, hosted=hosted)
        if prediction:
            logging.info("Prediction found")
            return prediction.json()
        else:
            logging.error("No prediction found")
            return None

    def parse_prediction(self, prediction: dict):
        return prediction["predictions"][0]["predicted_classes"][0]
    
    def start(self, image_url: str):
        prediction = self.predict(image_url=image_url, hosted=True)
        parsed_prediction = self.parse_prediction(prediction=prediction)
        return parsed_prediction
