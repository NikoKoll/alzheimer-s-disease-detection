import tensorflow as tf
from tensorflow import keras
from keras.models import load_model
from keras.preprocessing import image
import numpy as np

# Load the model
model = load_model('models/my_model.h5')

# Define the class labels for Alzheimer's disease
class_labels = ['Non-Demented', 'Mild Demented', 'Moderate to Severe Demented']

import cv2

def preprocess_image(img_path):
    img = cv2.imread(img_path)  # Load the image using OpenCV
    img = cv2.resize(img, (224, 224))  # Resize the image to (224, 224)
    img_array = img.astype(np.float32) / 255.0  # Convert to float32 and normalize
    img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension
    return img_array



def predict(img_path):
    processed_image = preprocess_image(img_path)
    prediction = model.predict(processed_image)
    print("Prediction:", prediction)  # Print the predicted class index
    predicted_class = np.argmax(prediction, axis=1)[0]  # Get the index of the highest probability
    print("Predicted class index:", predicted_class)  # Print the predicted class index

    # Map predicted class index to human-readable class label
    if predicted_class == 0:
        readable_prediction = 'Mild Demented'
    elif predicted_class == 1:
        readable_prediction = 'Moderate Demented'
    elif predicted_class == 2:
        readable_prediction = 'Non-Demented'
    elif predicted_class == 3:
        readable_prediction = 'Very Mild Demented'  # This category was introduced for the fourth category
    else:
        readable_prediction = 'Unknown'

    return readable_prediction

