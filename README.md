# Military Plane Classifier

This project is an image classifier designed to identify various types of military planes, including Fighter Jets, Bombers, Cargo Planes, Drones, Reconnaissance planes, and Trainer Jets. The classifier is built using deep learning techniques and is trained on a dataset of images categorized by plane type.

## Project Structure

```
military-plane-classifier
├── data
│   ├── fighter_jet
│   ├── bomber
│   ├── cargo_plane
│   ├── drone
│   ├── reconnaissance
│   └── trainer_jet
├── src
│   ├── model.py
│   ├── train.py
│   ├── predict.py
│   └── utils.py
├── requirements.txt
└── README.md
```

## Dataset

The dataset is organized into subdirectories within the `data` folder, with each subdirectory containing images of a specific type of military plane. The categories are as follows:

- `fighter_jet`: Images of fighter jets.
- `bomber`: Images of bombers.
- `cargo_plane`: Images of cargo planes.
- `drone`: Images of drones.
- `reconnaissance`: Images of reconnaissance planes.
- `trainer_jet`: Images of trainer jets.

## Setup Instructions

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/military-plane-classifier.git
   cd military-plane-classifier
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. **Training the Model**:
   To train the model, run the following command:
   ```
   python src/train.py
   ```

2. **Making Predictions**:
   After training, you can use the model to make predictions on new images:
   ```
   python src/predict.py --image path/to/image.jpg
   ```

## Model Architecture

The model architecture is defined in `src/model.py`, where the `PlaneClassifier` class is implemented. This class includes methods for building and compiling the model.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.