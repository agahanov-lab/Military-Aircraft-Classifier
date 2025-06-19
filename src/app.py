"""
Streamlit web app for military plane classification and dataset building
Created by Mekan Agahanov – now with image uploader for your dataset!
"""

import streamlit as st
import numpy as np
import os
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from datetime import datetime

class_names = ['Bombers', 'Fighter Jets', 'Reconnaissances']

@st.cache_resource
def load_classifier():
    return load_model('military_plane_classifier_model.h5')

model = load_classifier()

st.title("Military Plane Classifier")
st.write("Upload an image of a military plane and let a model do the guessing. No pilots were harmed in the making of this app.")

# --- Classifier Section ---
st.header("Classify a Plane Image")
uploaded_file = st.file_uploader("Choose an image to classify...", type=["jpg", "jpeg", "png"], key="classify")

if uploaded_file is not None:
    img = image.load_img(uploaded_file, target_size=(224, 224))
    st.image(img, caption='Uploaded Image', use_column_width=True)
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = img_array / 255.0

    preds = model.predict(img_array)
    pred_class = class_names[np.argmax(preds)]
    confidence = np.max(preds)
    st.write(f"**Prediction:** {pred_class} ({confidence:.2f} confidence)")
    st.write("Powered by Mekan Agahanov's code. If it's wrong, blame the AI, not Mekan!")

# --- Dataset Builder Section ---
st.header("Contribute to the Dataset!")
st.write("Help Mekan's AI get smarter. Upload a new plane image to the dataset:")

category = st.selectbox("Select category for your image:", class_names)
data_upload = st.file_uploader("Choose an image to add to the dataset...", type=["jpg", "jpeg", "png"], key="dataset")

if data_upload is not None and category:
    # Make sure the data directory exists
    save_dir = os.path.join("data", category)
    os.makedirs(save_dir, exist_ok=True)
    # Create a unique filename
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S%f")
    ext = os.path.splitext(data_upload.name)[1]
    save_path = os.path.join(save_dir, f"{timestamp}{ext}")
    # Save the file
    with open(save_path, "wb") as f:
        f.write(data_upload.getbuffer())
    print(f"Saved image to: {os.path.abspath(save_path)}")
    st.success(f"Image saved to `{save_dir}`! Thanks for helping Mekan's AI take over the skies! 🚀")