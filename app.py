import os
from flask import Flask, render_template, request, flash, redirect, url_for, send_from_directory
from flask_login import login_user, login_required, logout_user, current_user
import cv2
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.applications.resnet50 import preprocess_input
from db import app, db, bcrypt, User, RegisterForm, LoginForm

# Set the upload folder
UPLOAD_FOLDER = 'upload/'  # Ensure this folder exists
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['TEMPLATES_AUTO_RELOAD'] = True  # Ensure templates auto-reload

# Load your pre-trained model
model = load_model('C:/Users/felix/Downloads/age_prediction_model_resnet2.keras')  # Replace with your model path

def predict_age(image_path):
    # Load and preprocess the image
    img = cv2.imread(image_path)
    img_resized = cv2.resize(img, (224, 224))
    img_resized = np.array(img_resized, dtype=np.float32)
    img_resized = preprocess_input(img_resized)
    img_resized = np.expand_dims(img_resized, axis=0)

    # Predict the age
    predicted_age = model.predict(img_resized)
    print(f"Predicted age (raw): {predicted_age}")
    return round(float(predicted_age[0][0]))

# Route to serve the uploaded files
@app.route('/upload/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            return redirect(url_for('index'))
        else:
            flash('Invalid username or password. Please try again.', 'error')
    return render_template('login.html', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        new_user = User(username=form.username.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/index', methods=['GET', 'POST'])
@login_required
def index():
    return render_template('index.html')

@app.route('/tryit', methods=['GET', 'POST'])
@login_required
def try_it():
    age = None  # Set age to None initially
    image_url = None  # Set image_url to None initially
    return render_template('tryit.html', age=age, image_url=image_url)

@app.route('/predict', methods=['POST'])
@login_required
def predict():
    age = None  # Initialize age to None
    image_url = None  # Initialize image_url to None

    if 'image' not in request.files:
        flash('No file part', 'error')
        return render_template('tryit.html', age=age, image_url=image_url)

    file = request.files['image']
    if file.filename == '':
        flash('No selected file', 'error')
        return render_template('tryit.html', age=age, image_url=image_url)

    if file:
        # Save the file to the upload folder
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_path)
        print(f"File saved to: {file_path}")  # Debugging line

        # Generate the image URL for display
        image_url = url_for('uploaded_file', filename=file.filename)
        
        # Predict the age
        predicted_age = predict_age(file_path)
        age = predicted_age  # Set age to the predicted value
        print(f"Predicted Age: {age}")  # Debugging line

    # Render the template with the predicted age and image URL
    return render_template('tryit.html', age=age, image_url=image_url)

@app.route('/about-us')
def about_us():
    return render_template('about-us.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/how-it-works')
def how_it_works():
    return render_template('how-it-works.html')

if __name__ == '__main__':
    app.run(debug=True)
