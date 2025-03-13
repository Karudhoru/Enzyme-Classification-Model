# Enzyme Classification Project

Welcome to the Enzyme Classification Project! This repository contains a comprehensive toolkit for classifying enzymes, including theoretical background, data, models, and environment setup instructions. Whether you are a researcher, developer, or student, this project is designed to be accessible and easy to navigate.

---

## Table of Contents

- [Project Overview](#project-overview)
- [Repository Structure](#repository-structure)
- [Getting Started](#getting-started)
  - [Environment Setup](#environment-setup)
  - [Data Overview](#data-overview)
  - [Model Files](#model-files)
  - [Interactive Notebooks](#interactive-notebooks)
- [Documentation](#documentation)
- [Contributing](#contributing)
- [License](#license)

---

## Project Overview

This project is dedicated to the analysis and study of enzyme function, classification, and kinetics. It includes:
- **Theoretical Insights:** Detailed explanations about enzyme mechanisms, classifications, and functions.
- **Data Resources:** A curated dataset (`Enzyme Data.tsv`) that provides enzyme-specific information.
- **Pre-Trained Models:** Models and vectorizers for enzyme analysis saved in a serialized format.
- **Interactive Analysis:** Jupyter notebooks for modeling and exploratory analysis.

Our aim is to make advanced enzyme research accessible and reproducible by providing a well-documented repository and a complete setup for data analysis and modeling.

---

## Repository Structure

The repository is organized into several key directories:
```plain text
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

- **Data:**  
  Contains the enzyme dataset (`Enzyme Data.tsv`) which serves as the foundation for all analyses.

- **Docs:**  
  Provides theoretical background on enzymes and a detailed description of their classifications, functions, and the data sources used. Both Markdown and PDF formats are available.

- **Environment:**  
  Includes everything needed to set up the project’s working environment:
  - `environment.yml` for creating a Conda environment with all dependencies.
  - Detailed installation guides (`INSTALLATION.pdf`) to help you get started.

- **Model:**  
  Contains the pre-trained model and its corresponding vectorizer. These files are used to perform enzyme analysis and predictions.

- **bin:**  
  Features an interactive Jupyter Notebook (`model.ipynb`) for running experiments, visualizing data, and further exploring the model.

---

## Getting Started

### Environment Setup

1. **Clone the Repository:**
```bash
   git clone https://github.com/Karudhoru/Enzyme-Classification-Model.git
   cd "Enzyme Classification Model"
```

2. **Create the Conda Environment: Navigate to the Environment directory and run:**
```bash
    conda env create -f environment.yml
```
  Then activate the environment:
```bash
    conda activate enzyme_classification
```
  For detailed installation instructions, refer to the Environment/INSTALLATION.pdf.

3. **Data Overview**
  The enzyme dataset can be found in the Data folder:

  Enzyme Data.tsv: Contains curated enzyme data, including enzyme IDs, names, classifications, functions, and other biochemical properties.

4. **Model Files**
  The pre-trained model and vectorizer are stored in the Model folder:

  model.pkl: Serialized machine learning model for enzyme analysis.
  vectorizer.pkl: Preprocessed vectorizer that transforms input data into a format suitable for the model.

5. **Documentation**
  Further documentation is available in the Docs folder:

  THEORY.pdf: Provides an in-depth theoretical background on enzymes, including classifications, mechanisms, and data sources.
  INSTALLATION.pdf: Guides you through the installation and environment setup process.
  These documents serve as a valuable resource for understanding both the scientific and technical aspects of the project.

Thank you for your interest in the Enzyme Analysis Project! If you have any questions or need further assistance, please refer to the documentation or open an issue on GitHub.







