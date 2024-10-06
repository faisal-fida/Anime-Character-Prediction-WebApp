# Anime Character Prediction WebApp

This project is a web application that predicts anime characters using machine learning models. It leverages Flask for the web framework and Roboflow for the ML model predictions.

## Features

- **Simple User Interface**: Users can upload an image or provide an image URL to get predictions.
- **Model Integration**: Utilizes Roboflow's API to predict anime characters.
- **Dynamic Rendering**: Results are dynamically rendered on the web page using Flask templating.

## File Structure

- `app.py`: Main application file using Flask to set up routes for GET and POST requests.
- `ml_model.py`: Contains the `Predictions` class that interfaces with the Roboflow API to make predictions.
- `templates/index.html`: HTML template for the web application interface.

## Key Components

### Flask Application (`app.py`)

- **Endpoints**:
  - `GET /`: Renders the main page.
  - `POST /`: Handles image URL submissions and returns prediction results.
- **Server Configuration**: Runs the server on `port 1200` with debug mode enabled.

### Machine Learning Model (`ml_model.py`)

- **Prediction Class**:
  - `predict`: Calls Roboflow API to get predictions.
  - `parse_prediction`: Extracts the relevant prediction result.
  - `start`: Orchestrates the prediction process.

### HTML Template (`templates/index.html`)

- **Forms**: Two forms for different anime series (One Piece, Naruto) allowing users to upload an image or enter an image URL.
- **Dynamic Results**: Displays the prediction results dynamically based on the user input.

## Challenges and Solutions

- **API Integration**: Integrating with Roboflow's API required careful handling of API keys and project setup.
- **Dynamic Rendering**: Ensuring the prediction results are dynamically rendered on the same page using Flask templating.
- **Error Handling**: Implementing logging to handle and debug prediction errors effectively.

## Getting Started

1. Clone the repository.
2. Install the required dependencies.
3. Set up environment variables for the Roboflow API key and project name.
4. Run the Flask app.

```bash
git clone https://github.com/faisal-fida/Anime-Character-Prediction-WebApp.git
cd Anime-Character-Prediction-WebApp
pip install -r requirements.txt
export ROBOFLOW_API_KEY=your_api_key
export ROBOFLOW_PROJECT_NAME=your_project_name
python app.py
```

## Conclusion

This project demonstrates a practical application of integrating machine learning models into a web application, showcasing the use of Flask and Roboflow to predict anime characters from images. The project highlights the complexities of API integration, dynamic content rendering, and error handling.

Feel free to contribute or raise issues if you encounter any problems!
