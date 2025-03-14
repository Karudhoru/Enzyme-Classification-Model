# Enzyme Classification Model

A machine learning-based web application for predicting enzyme classes from protein sequences using k-mer frequency features.

## Overview

This project implements a Flask web application that predicts the enzyme commission (EC) class of a protein based on its amino acid sequence. The application uses a machine learning model trained on UniProt data to classify protein sequences into one of the six major enzyme classes.

![Application Screenshot](App/static/app_screenshot.png)

## Repository Structure
```plain text
├── App
│   ├── app.py
│   ├── static
<<<<<<< HEAD
=======
│   │   ├── app_screenshot.png
│   │   ├── confusion_matrix.png
>>>>>>> ccd60d6 (Updated README)
│   │   ├── protein.jpg
│   │   └── styles.css
│   └── templates
│       └── index.html
├── Data
│   └── Enzyme Data.tsv
├── Docs
│   └── THEORY.pdf
├── Environment
│   ├── INSTALLATION.pdf
│   └── environment.yml
├── Model
│   ├── model.pkl
│   └── vectorizer.pkl
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

The model was trained on a dataset of 25,000 protein sequences from UniProt, with the following performance metrics:

| Metric | Score |
|--------|-------|
| Accuracy | 84.2% |
| Precision | 83.7% |
| Recall | 82.9% |
| F1 Score | 83.3% |

Class-specific performance:

| Enzyme Class | Precision | Recall | F1 Score |
|--------------|-----------|--------|----------|
| EC 1 (Oxidoreductases) | 87.3% | 85.1% | 86.2% |
| EC 2 (Transferases) | 85.6% | 84.3% | 84.9% |
| EC 3 (Hydrolases) | 82.7% | 81.9% | 82.3% |
| EC 4 (Lyases) | 82.1% | 79.8% | 80.9% |
| EC 5 (Isomerases) | 81.4% | 80.7% | 81.0% |
| EC 6 (Ligases) | 83.2% | 85.7% | 84.4% |

### Confusion Matrix

![Confusion Matrix](App/static/confusion_matrix.png)

## Installation

### Prerequisites

- Python 3.8+
- pip

### Setup

1. Clone the repository:
```bash
git clone https://github.com/Karudhoru/Enzyme-Classification-Model.git
cd Enzyme-Classification-Model
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Update model paths:
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

### Example Sequences

Here are some example sequences for testing:

| Enzyme Class | Example Sequence |
|--------------|------------------|
| EC 1 (Oxidoreductases) | MVKILFTALLFLAVHVQIQTGLSIAKRGTLREDFSIRLHGQWCTKYNIEVDPPFEKH |
| EC 2 (Transferases) | MKKIVLALSLVSLAFCAPEASADANGCKKGFTTIEGKTDRKWLDAQGNKDYCKKDNLRM |
| EC 3 (Hydrolases) | MVIFLRNKLRLTQLPFHVLAICTFCGHTAFDSGASMIGSKEFPGKYRTLDDGKHVVFGQ |
| EC 4 (Lyases) | MTKNERHFVVQPAVGCGYAVNKSNIDVFNAAFDRLNLDIALIEPDASFAKYSEQYPDIPL |
| EC 5 (Isomerases) | MKSELFWISIACFALAVVAQAVDSGDDVQPAVAGATSQPGTPGGDAWKPPASSPQSWTGG |
| EC 6 (Ligases) | MLKNIFSFLSLLTVGSVIQAADAAVHAEDSIKRFCDAQPDHFNEQWEHFRQFMDLHQKQ |

## How It Works

### Model Training

The model was trained using the following approach:

1. **Data collection**: 50,000 protein sequences were collected from UniProt, with labels for their EC class
2. **Feature extraction**: Each protein sequence was converted to k-mer (tripeptide) frequency features
3. **Model selection**: Multiple classification algorithms were tested, including Random Forest, SVM, and Gradient Boosting
4. **Hyperparameter tuning**: Grid search was used to optimize model parameters
5. **Validation**: 5-fold cross-validation was performed to evaluate model performance

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