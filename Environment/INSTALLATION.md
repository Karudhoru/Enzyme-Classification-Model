# Installation and Environment Setup

This document provides step-by-step instructions to install and use the Conda environment for this project. The environment is defined in the `environment.yml` file and includes all necessary dependencies such as Python, NumPy, Pandas, Matplotlib, Seaborn, scikit-learn, and JupyterLab.

## Prerequisites

- **Conda Installed:**  
  Ensure you have [Conda](https://docs.conda.io/en/latest/) installed. You can use either [Anaconda](https://www.anaconda.com/products/distribution) or [Miniconda](https://docs.conda.io/en/latest/miniconda.html).

## Steps to Install the Environment

1. **Create the Conda Environment**

    Run the following command from the root directory where the environment.yml file is located:
```bash
    conda env create -f environment.yml
```
    This command creates a new Conda environment named enzyme_classification with all the required dependencies.

2. **Activate the Environment**

    Once the environment is created, activate it using:
```bash
    conda activate enzyme_analysis
```

3. **Deactivating the Environment**

    When you are done working, you can deactivate the environment with:
```bash
    conda deactivate
```







