import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
import joblib
import os

# Define the relative file paths (only using ChatGPT and Claude datasets)
datasets = {
    "chatgpt": os.path.join("datasets", "chatgpt.xlsx"),
    "claude": os.path.join("datasets", "claude.xlsx")
}

# Define the SVM classifier
classifier = SVC(probability=True)

# Function to train the model
def train_model():
    # Iterate over each dataset (now only ChatGPT and Claude)
    for dataset_name, file_path in datasets.items():
        # Load the dataset
        data = pd.read_excel(file_path)

        # Select relevant columns (using original column names)
        data_filtered = data[['Token-level Accuracy', 'Naturalness', 'Source']]

        # Filter for HCT and MGT labels in the 'Source' column
        data_filtered = data_filtered[data_filtered['Source'].isin(['HCT', 'MGT'])]

        # Calculate perturbation discrepancy as the absolute difference between 'Token-level Accuracy' and 'Naturalness'
        data_filtered['Perturbation Discrepancy'] = np.abs(data_filtered['Token-level Accuracy'] - data_filtered['Naturalness'])

        # Prepare the input features and output target
        X = data_filtered[['Token-level Accuracy', 'Naturalness', 'Perturbation Discrepancy']]
        y = data_filtered['Source']

        # Encode the categorical target variable (HCT, MGT)
        label_encoder = LabelEncoder()
        y_encoded = label_encoder.fit_transform(y)  # HCT -> 0, MGT -> 1

        # Split the data into train and test sets with a 50:50 ratio
        X_train, X_test, y_train, y_test = train_test_split(X, y_encoded, test_size=0.5, random_state=42)

        # Scale the input features
        scaler = StandardScaler()
        X_train_scaled = scaler.fit_transform(X_train)
        
        # Train the model
        classifier.fit(X_train_scaled, y_train)

        # Save the trained model to disk
        model_file_path = os.path.join("models", f"{dataset_name}_svm_model.pkl")
        joblib.dump(classifier, model_file_path)
        print(f"Model for {dataset_name} saved at: {model_file_path}")

# Run the training process
if not os.path.exists("models"):
    os.makedirs("models")
train_model()
