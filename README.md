# Military Aircraft Classifier  
Created by Mekan Agahanov

Ever wondered if that plane is a bomber, a fighter jet, or a reconnaissance marvel?

---

## Project Structure

```
military-plane-classifier
├── data
│   ├── Bombers
│   ├── Fighter Jets
│   └── Reconnaissances
├── src
│   ├── model.py
│   ├── train.py
│   ├── predict.py
│   ├── app.py
│   └── utils.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

## Features

- **Classifies images** as **Bombers**, **Fighter Jets**, or **Reconnaissances**
- **Transfer learning** with ResNet50 for robust performance
- **Streamlit web app** for easy image classification and dataset building
- **Command-line prediction** for quick checks
- **Personalized and humorous interface**—because AI should be fun!

---

## Dataset

The dataset is organized into subdirectories within the `data` folder, with each subdirectory containing images of a specific type of military plane:

- `Bombers`: Images of bombers.
- `Fighter Jets`: Images of fighter jets.
- `Reconnaissances`: Images of reconnaissance planes.

> **Note:** Do **not** upload your full dataset to GitHub. Only include a few sample images if you want.

---

## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/agahanov-lab/Military-Aircraft-Classifier.git
   cd Military-Aircraft-Classifier
   ```

2. **Install the required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

---

## Usage

### 1. **Train the Model (Optional)**
If you want to train the model with your own images:
- Place your images in the appropriate `data/<Category>/` folders.
- Run:
  ```bash
  python src/train.py
  ```

### 2. **Classify Images via Web Interface**
- Start the Streamlit app:
  ```bash
  streamlit run src/app.py
  ```
- In your browser, upload an image in the "Classify a Plane Image" section.
- See the prediction and confidence score (0–1, where 1 means the AI is 100% sure).

### 3. **Contribute to the Dataset via Web Interface**
- In the Streamlit app, scroll to "Contribute to the Dataset!"
- Select a category and upload an image.
- The image will be saved to the corresponding folder in `data/` for future training.

### 4. **Command-Line Prediction**
- Predict the class of a new image:
  ```bash
  python src/predict.py path/to/image.jpg
  ```

---

## What does "confidence" mean?

- The confidence score is a number between **0 and 1** (e.g., 0.87 means 87% sure).
- The higher the confidence, the more certain the AI is about its guess.
- If the confidence is low, the AI is basically shrugging and saying, "I'm not sure, but here’s my best guess!"

---

## Model Architecture

The model architecture is defined in `src/model.py` as the `PlaneClassifier` class, using ResNet50 as a feature extractor and a custom classification head.

---

## Contributing

Contributions are welcome!  
Feel free to submit a pull request or open an issue for suggestions, improvements, or new plane categories.

---

**Happy plane spotting!**  
*If the classifier is wrong, blame the AI, not Mekan!
