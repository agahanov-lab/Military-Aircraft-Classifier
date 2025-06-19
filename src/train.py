"""
Train your military plane classifier with Mekan Agahanov's secret recipe.
Warning: May cause sudden urge to spot planes at airports.
"""

import os
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from model import PlaneClassifier

def load_data(data_dir, img_size=(224, 224), batch_size=32):
    print("I'm looking for data directory at:", os.path.abspath(data_dir))
    if not os.path.exists(data_dir):
        raise FileNotFoundError(f"Data directory not found: {os.path.abspath(data_dir)}. Did you forget to salute?")
    datagen = ImageDataGenerator(
        rescale=1./255,
        validation_split=0.2
    )
    train_generator = datagen.flow_from_directory(
        data_dir,
        target_size=img_size,
        batch_size=batch_size,
        class_mode='categorical',
        subset='training',
        shuffle=True
    )
    val_generator = datagen.flow_from_directory(
        data_dir,
        target_size=img_size,
        batch_size=batch_size,
        class_mode='categorical',
        subset='validation',
        shuffle=True
    )
    return train_generator, val_generator

def train_model(train_generator, val_generator, epochs=10):
    num_classes = train_generator.num_classes
    model = PlaneClassifier(num_classes=num_classes).model
    model.compile(
        optimizer='adam',
        loss='categorical_crossentropy',
        metrics=['accuracy']
    )
    print("Training initiated! Fasten your seatbelts!")
    model.fit(
        train_generator,
        validation_data=val_generator,
        epochs=epochs
    )
    model.save('military_plane_classifier_model.h5')
    print("Model saved as 'military_plane_classifier_model.h5'. Mekan salutes you!")

if __name__ == "__main__":
    data_directory = 'data'
    train_data, val_data = load_data(data_directory)
    train_model(train_data, val_data, epochs=8)