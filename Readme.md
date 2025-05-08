# DiscrimText: A Multi-Feature Framework for Enhanced Detection of Machine-Generated Text

DiscrimText is a novel approach for detecting machine-generated text (MGT) produced by large language models (LLMs) like ChatGPT, Claude, and others. Unlike traditional detection methods that rely on isolated linguistic features or simple probabilistic metrics, DiscrimText integrates three key features to improve detection performance:

- **Naturalness**: Quantifies the linguistic predictability of the text.
- **Performance**: Measures the accuracy of text-completion models on the text.
- **Perturbation Discrepancy**: Evaluates the sensitivity of the text to minor perturbations.

This repository contains the implementation of the DiscrimText framework, which combines these features into a machine learning model for classifying text as either human-generated or machine-generated.

## Features

- **Naturalness Calculation**: Based on n-gram and cache models to quantify text predictability.
- **Performance Assessment**: Uses token-level accuracy from text-completion models.
- **Perturbation Discrepancy**: Measures the change in log probability when the text is perturbed.

## Installation

### Prerequisites

- Python 3.7 or later
- pip
- scikit-learn
- numpy
- pandas

### Steps to Install

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/discrimtext.git
    cd discrimtext
    ```

2. Create a virtual environment:

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # For Linux/MacOS
    venv\Scripts\activate     # For Windows
    ```

3. Install required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

### Data Preparation

Before using the model, you'll need a dataset containing both human-generated text (HGT) and machine-generated text (MGT). You can use publicly available datasets or generate your own by running a language model like ChatGPT or Claude. The datasets should be balanced with equal samples of HGT and MGT.

### Feature Computation

DiscrimText uses three features to train the classifier:

1. **Naturalness**: Compute the naturalness of the text using a blend of global n-gram and local cache models.
2. **Performance**: Measure the token-level accuracy of a standard text-completion model (e.g., GPT-3).
3. **Perturbation Discrepancy**: Calculate the log probability difference between the original and perturbed versions of the text.

### Training the Classifier

Once the features are computed, you can train the Support Vector Machine (SVM) classifier:

```bash
python train.py --train_data <path_to_training_data>
