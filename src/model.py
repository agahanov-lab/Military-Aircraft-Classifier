"""
Military Plane Classifier by Mekan Agahanov
Because even AI should know its bombers from its jets!
"""

from tensorflow.keras import layers, models
from tensorflow.keras.applications import ResNet50

class PlaneClassifier:
    def __init__(self, num_classes):
        """
        Initialize the Mekan Agahanov's legendary plane classifier.
        """
        self.num_classes = num_classes
        self.model = self.build_model()

    def build_model(self):
        base_model = ResNet50(weights='imagenet', include_top=False, input_shape=(224, 224, 3))
        base_model.trainable = False  # Sorry, ResNet50, you get to chill.

        model = models.Sequential([
            base_model,
            layers.GlobalAveragePooling2D(),
            layers.Dense(128, activation='relu'),
            layers.Dense(self.num_classes, activation='softmax')
        ])
        return model

    def compile_model(self):
        self.model.compile(
            optimizer='adam',
            loss='categorical_crossentropy',
            metrics=['accuracy']
        )