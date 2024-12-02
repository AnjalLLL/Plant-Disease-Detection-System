import tensorflow as tf
import os
import numpy as np
import joblib
import tensorflow as tf
from keras.preprocessing import image
from tensorflow.keras.preprocessing import image  # Correct import
import numpy as np


# Paths to the saved models
CNN_MODEL_PATH = os.path.join("myapp", "modals", "fix_model.h5")
RF_MODEL_PATH = os.path.join("myapp", "modals", "rf_fix_model.pkl")
class_names = ['Apple___Apple_scab', 'Apple___Black_rot', 'Apple___Cedar_apple_rust', 'Apple___healthy', 'Corn___Cercospora_leaf_spot Gray_leaf_spot', 'Corn___Common_rust', 'Corn___Northern_Leaf_Blight', 'Corn___healthy', 'Grape___Black_rot', 'Grape___Esca_(Black_Measles)', 'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)', 'Grape___healthy', 'Tomato___Bacterial_spot', 'Tomato___Early_blight', 'Tomato___Late_blight', 'Tomato___Leaf_Mold', 'Tomato___Septoria_leaf_spot', 'Tomato___Spider_mites Two-spotted_spider_mite', 'Tomato___Target_Spot', 'Tomato___Tomato_Yellow_Leaf_Curl_Virus', 'Tomato___Tomato_mosaic_virus', 'Tomato___healthy']
# Load the models
cnn_model = tf.keras.models.load_model(CNN_MODEL_PATH, compile=False)
cnn_model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

rf_model = joblib.load(RF_MODEL_PATH)

feature_extractor = tf.keras.Model(
    inputs=cnn_model.inputs,
    outputs=cnn_model.layers[-2].output  # Output of the layer before the final classification layer
)

# Function to preprocess the image
def preprocess_image(img_path):
    img = image.load_img(img_path, target_size=(180, 180))  # Adjust target size if needed
    img = image.img_to_array(img)
    img = np.expand_dims(img, axis=0)
    img = img / 255.0  # Normalize the image
    return img


def extract_features(img):
    """Extract features using the CNN model."""
    features = feature_extractor.predict(img)
    features = features.reshape(features.shape[0], -1)
    return features

def predict(file_path):
    """Predict the class of the given image."""
    img_array = preprocess_image(file_path)
    features = extract_features(img_array)
    prediction = rf_model.predict(features)
    
    # Check the prediction output shape, it should be a single value (index)
    print(f"Prediction raw output: {prediction}")
    
    # If the prediction is in 2D, access the scalar value
    predicted_class_idx = prediction[0] if prediction.ndim == 1 else prediction[0][0]

    # Map the prediction index to class name
    predicted_class = class_names[predicted_class_idx]

    print(f"Predicted class: {predicted_class}")  # Debugging output
    return predicted_class

