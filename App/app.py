import joblib
from flask import Flask, render_template, request

app = Flask(__name__)

# Load the trained model and vectorizer
model = joblib.load("D:/GIT/Enzyme Classification/Model/model.pkl")
vectorizer = joblib.load("D:/GIT/Enzyme Classification/Model/vectorizer.pkl")

# Mapping of EC classes to names and functions
ec_class_info = {
    1: {"name": "Oxidoreductases", "function": "Catalyze oxidation-reduction reactions"},
    2: {"name": "Transferases", "function": "Transfer functional groups"},
    3: {"name": "Hydrolases", "function": "Catalyze hydrolysis of various bonds"},
    4: {"name": "Lyases", "function": "Catalyze the breaking of various bonds by means other than hydrolysis and oxidation"},
    5: {"name": "Isomerases", "function": "Catalyze isomerization changes within a single molecule"},
    6: {"name": "Ligases", "function": "Join two molecules with covalent bonds"}
}

def get_class_info(class_number):
    """Retrieve the name and function of the enzyme class."""
    info = ec_class_info.get(class_number, {"name": "Unknown", "function": "Unknown"})
    return info["name"], info["function"]

def predict_class(sequence):
    """Predict the enzyme class for a given protein sequence."""
    sequence = sequence.strip().upper()
    # Validate the sequence
    if not all(c in 'ACDEFGHIKLMNPQRSTVWY' for c in sequence):
        return {"error": "Invalid sequence. Only standard amino acids allowed."}
    if len(sequence) < 3:
        return {"error": "Sequence must be at least 3 amino acids long."}
    # Transform sequence to 3-mer frequencies and predict
    counts = vectorizer.transform([sequence])
    freq = counts / counts.sum(axis=1)
    class_number = model.predict(freq)[0]
    class_name, major_function = get_class_info(class_number)
    return {
        "class_number": class_number,
        "class_name": class_name,
        "major_function": major_function
    }

@app.route('/')
def home():
    """Render the home page."""
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    """Handle prediction requests."""
    sequence = request.form['sequence']
    prediction = predict_class(sequence)
    return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)