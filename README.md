# Intro to AI

> A hands-on learning repository for core AI, machine learning, and deep learning concepts.

## Overview

This repository is organized as a study path across the main foundations of AI:

- Python basics and data handling
- Linear algebra, calculus, and probability/statistics
- Classical machine learning algorithms
- PyTorch, tensors, neural networks, and training loops
- Practice notebooks and small Python mini projects

## Project Structure

```
intro_to_AI/
├── Calculus_for_AI/
├── dataset_analysis/
├── data/
├── docs/
├── linear_algebra/
├── machine_learning/
├── mini_projects/
├── models/
├── optimization/
├── probability_and_statistics/
├── pytorch/
└── README.md
```

## Highlights

- `Calculus_for_AI/`: derivatives, gradients, multivariable functions, and partial derivatives
- `linear_algebra/`: vectors, matrices, norms, rank, eigenvalues, and eigenvectors
- `probability_and_statistics/`: probability, distributions, and basic statistics
- `dataset_analysis/`: notebook-based data exploration and analysis
- `machine_learning/`: regression, classification, clustering, feature engineering, and model evaluation
- `optimization/`: loss functions, gradient descent, SGD, and Adam
- `pytorch/`: tensors, autograd, training examples, and FashionMNIST
- `mini_projects/`: practical console apps and end-to-end mini projects
- `docs/`: supporting documentation, including the PyTorch guide

## Getting Started

### 1. Create and activate a virtual environment

Recommended Python version: 3.10.11

```bash
python -m venv .venv
.venv\Scripts\activate
```

If you are on macOS or Linux, use:

```bash
source .venv/bin/activate
```

### 2. Install dependencies

```bash
pip install torch torchvision torchaudio
pip install jupyter numpy pandas matplotlib seaborn scikit-learn
```

If you use a GPU, install the PyTorch build that matches your CUDA version from the official PyTorch website.

### 3. Verify PyTorch and CUDA

Run the check script from the `mini_projects/` folder:

```bash
python mini_projects/check.py
```

This prints the installed PyTorch version, CUDA availability, and GPU details when available.

### 4. Open notebooks

```bash
jupyter notebook
```

Then open any notebook you want to study, for example:

- `pytorch/fashionMNISTImageClassifier.ipynb`
- `machine_learning/machine_learning_algorithms/logistic_regression.ipynb`
- `linear_algebra/vector.ipynb`
- `Calculus_for_AI/derivative.ipynb`

### 5. Run the mini projects

The console apps use local imports, so run them from inside their own folders:

```bash
cd mini_projects\employee_management
python main.py
```

```bash
cd mini_projects\mini_project_student
python main.py
```

## Data and Models

- `data/` contains sample datasets such as Titanic, Diabetes, FashionMNIST, email spam, employees, and students
- `models/` stores saved models and checkpoints used by selected notebooks and mini projects

## Reference Material

- `docs/pytorch.md`: a Vietnamese PyTorch study guide
- [PyTorch Docs](https://pytorch.org/docs/)
- [PyTorch Tutorials](https://pytorch.org/tutorials/)

## Notes

- This is a learning repository, so clarity and experimentation matter more than production hardening
- Many notebooks are designed to be edited and rerun while you change epochs, learning rate, batch size, or model architecture
- In VS Code, make sure the Python interpreter points to the project `.venv` so notebooks and scripts use the same environment
