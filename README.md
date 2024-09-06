# Age Prediction Web Application

This project is a Flask-based web application that predicts the age of a person from an uploaded video file. The application leverages the power of deep learning models, specifically ResNet50, to analyze facial features and estimate age. The application is deployed on AWS EC2 with NGINX serving as a reverse proxy.

## Features
- User Interface: Users can upload video files directly through the web interface.
- Age Prediction: Utilizes a pre-trained ResNet50 model to predict age from facial features in video frames.
- Responsive Design: The web application is responsive and works across various devices.
- Deployment: The application is deployed on AWS EC2 using NGINX as a reverse proxy for handling requests.

## Architecture
The application is built with a clear separation of concerns:

### Flask Web Application:
- Handles routing, user sessions, and orchestrates the data flow.
- Integrates with deep learning models for predicting age.

### Face Model:
- ResNet50: A deep learning model pre-trained on the ImageNet dataset, customized with additional layers to predict age based on facial features extracted from video frames.
- OpenCV: Used to process video frames and detect faces.

### Deployment:
- AWS EC2: The application is hosted on an Ubuntu instance in AWS EC2.
- Nginx: Serves as a reverse proxy, handling incoming HTTP requests and serving the Flask application.

## Getting Started
### Prerequisites
- Python 3.7+
- Flask
- TensorFlow
- OpenCV
- AWS Account

### Installation
1. Clone the Repository:

git clone https://github.com/felixjoseph1/age-prediction.git
cd age-prediction-webapp


2. Set Up Virtual Environment:

python3 -m venv venv
source venv/bin/activate


3. Install Dependencies:

pip install -r requirements.txt


4. Download the Pre-trained Model:
- Ensure you have the necessary pre-trained ResNet50 model weights.

5. Set Up Environment Variables:
- Create a .env file and add any necessary environment variables.

### Usage
1. Run the Application Locally:

python app.py


2. Access the Application:
- Open your browser and navigate to http://127.0.0.1:5000.

3. Upload Video and Get Prediction:
- Use the web interface to upload a video file and receive the age prediction.