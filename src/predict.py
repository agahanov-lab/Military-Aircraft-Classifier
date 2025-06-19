"""
Predict military plane types with Mekan Agahanov's classifier.
Warning: May cause spontaneous Top Gun quotes.
"""

import sys
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

class_names = ['Bomber', 'Fighter Jet', 'Reconnaissance']

def predict_image(img_path, model_path='military_plane_classifier_model.h5'):
    model = load_model(model_path)
    img = image.load_img(img_path, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = img_array / 255.0

    preds = model.predict(img_array)
    pred_class = class_names[np.argmax(preds)]
    confidence = np.max(preds)
    print(f"I say that it is a: {pred_class} (confidence: {confidence:.2f})")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python predict.py path_to_image.jpg\nBrought to you by Mekan.")
    else:
        predict_image(sys.argv[1])