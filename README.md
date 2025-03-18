# Enzyme Classification Model

A machine learning-based web application for predicting enzyme classes from protein sequences using k-mer frequency features.

## Overview

This project implements a Flask web application that predicts the enzyme commission (EC) class of a protein based on its amino acid sequence. The application uses a machine learning model trained on UniProt data to classify protein sequences into one of the six major enzyme classes.

![Application Screenshot](App/static/app_screenshot.png)

## Repository Structure
```plain text
├── App
│   ├── app.py
│   ├── static
│   │   ├── app_screenshot.png
│   │   ├── confusion_matrix.png
│   │   ├── roc_curves.png
│   │   ├── pr_curves.png
│   │   ├── protein.jpg
│   │   └── styles.css
│   └── templates
│       └── index.html
├── Data
│   └── Enzyme Data.tsv
├── Docs
│   └── THEORY.pdf
├── Environment
│   ├── INSTALLATION.pdf
│   └── environment.yml
├── Model
│   ├── model.pkl
│   └── vectorizer.pkl
├── README.md
└── bin
    └── model.ipynb
```

## Features

- Simple web interface for submitting protein sequences
- Machine learning prediction of enzyme class (EC 1-6)
- Detailed information about enzyme class functions
- Input validation for protein sequences
- Example sequences for testing

## Enzyme Classes

The model predicts proteins into one of six major enzyme classes:

1. **Oxidoreductases (EC 1)**: Catalyze oxidation-reduction reactions
2. **Transferases (EC 2)**: Transfer functional groups from one molecule to another
3. **Hydrolases (EC 3)**: Catalyze the hydrolysis of various bonds
4. **Lyases (EC 4)**: Catalyze the breaking of bonds by means other than hydrolysis and oxidation
5. **Isomerases (EC 5)**: Catalyze isomerization changes within a single molecule
6. **Ligases (EC 6)**: Join two molecules with covalent bonds

## Model Performance

The model was trained on an expanded dataset of protein sequences from UniProt, with the following performance metrics:

### Overall Metrics

| Metric | Score |
|--------|-------|
| Accuracy | 86.5% |
| Macro Precision | 94.3% |
| Macro Recall | 78.8% |
| Macro F1 Score | 85.0% |
| Average ROC AUC | 98.1% |

### Class-specific Performance

| Enzyme Class | Precision | Recall | F1 Score | ROC AUC | Support |
|--------------|-----------|--------|----------|---------|---------|
| EC 1 (Oxidoreductases) | 100.0% | 75.7% | 86.2% | 98.1% | 445 |
| EC 2 (Transferases) | 80.3% | 95.5% | 87.2% | 97.8% | 1308 |
| EC 3 (Hydrolases) | 88.3% | 84.4% | 86.3% | 98.0% | 1002 |
| EC 4 (Lyases) | 100.0% | 67.5% | 80.6% | 98.2% | 117 |
| EC 5 (Isomerases) | 99.1% | 82.7% | 90.2% | 98.6% | 133 |
| EC 6 (Ligases) | 98.8% | 66.9% | 79.8% | 97.8% | 118 |

### Confusion Matrix

```
[[ 337   84   24    0    0    0]
 [   1 1249   56    0    1    1]
 [   0  156  846    0    0    0]
 [   0   28   10   79    0    0]
 [   0   14    9    0  110    0]
 [   0   25   14    0    0   79]]
```

![Confusion Matrix](App/static/confusion_matrix.png)

### ROC Curves

![ROC Curves](App/static/roc_curves.png)

### Precision-Recall Curves

![Precision-Recall Curves](App/static/precision_recall_curves.png)

## Installation

### Prerequisites

- Conda (Anaconda or Miniconda)
- Git
### Setup

1. Clone the repository:
```bash
git clone https://github.com/Karudhoru/Enzyme-Classification-Model.git
cd Enzyme-Classification-Model
```

2. Create the Conda Environment: Navigate to the Environment directory and run:
```bash
conda env create -f Environment/environment.yml
```
Then, activate the environment:
```bash
conda activate enzyme_classification
```

3. Update model paths:
Edit `app.py` to use relative paths for model files:

```python
# Change these lines
model = joblib.load("D:/GIT/Enzyme Classification/Model/model.pkl")
vectorizer = joblib.load("D:/GIT/Enzyme Classification/Model/vectorizer.pkl")

# To these lines
model = joblib.load("Model/model.pkl")
vectorizer = joblib.load("Model/vectorizer.pkl")
```

## Usage

1. Start the application:
```bash
python app.py
```

2. Open your browser and navigate to:
```
http://127.0.0.1:5000/
```

3. Enter a protein sequence in the text area or click "Try an Example" to use a sample sequence.

4. Click "Predict" to get the enzyme class prediction.

## How It Works

### Model Training

The model was trained using the following approach:

1. **Data collection**: Protein sequences were collected from UniProt, with labels for their EC class
2. **Feature extraction**: Each protein sequence was converted to k-mer (tripeptide) frequency features
3. **Model selection**: Multiple classification algorithms were tested, including Random Forest, SVM, and Gradient Boosting
4. **Hyperparameter tuning**: Grid search was used to optimize model parameters
5. **Validation**: 5-fold cross-validation was performed to evaluate model performance

### Model Evaluation Script

The model evaluation script imports comprehensive metrics packages and calculates detailed performance metrics:

```python
# Import required metrics from sklearn
from sklearn.metrics import accuracy_score, f1_score, confusion_matrix
from sklearn.metrics import precision_score, recall_score
from sklearn.metrics import classification_report, roc_auc_score, roc_curve
from sklearn.metrics import precision_recall_curve, average_precision_score, auc

# Calculate basic metrics
accuracy = accuracy_score(y_test, y_pred)
precision_macro = precision_score(y_test, y_pred, average='macro')
recall_macro = recall_score(y_test, y_pred, average='macro')
f1_macro = f1_score(y_test, y_pred, average='macro')

# Generate detailed classification report
class_report = classification_report(y_test, y_pred)

# Calculate ROC AUC for each class
# Generate visualizations for analysis
```

### Performance Analysis

The model shows excellent precision for most enzyme classes, but recall varies more significantly:

- **High Precision Classes**: EC 1, EC 4, EC 5, and EC 6 all have precision values above 98%
- **Balanced Classes**: EC 3 (Hydrolases) shows the most balanced performance between precision and recall
- **Class Imbalance**: The dataset contains significantly more examples of EC 2 and EC 3 classes
- **ROC Performance**: All classes show excellent ROC AUC scores above 97.8%, indicating strong discriminative ability

### Prediction Process

The application processes protein sequences as follows:

1. User inputs a protein sequence
2. The sequence is validated for correct amino acid characters
3. The sequence is converted to 3-mer frequency features using the pre-trained vectorizer
4. The model predicts the enzyme class based on these features
5. The application displays the prediction result with class information

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## Contact

Project Link: [https://github.com/Karudhoru/Enzyme-Classification-Model](https://github.com/Karudhoru/Enzyme-Classification-Model)

## Acknowledgments

- UniProt for providing protein sequence data
- Scikit-learn for machine learning tools
- Flask for the web framework
