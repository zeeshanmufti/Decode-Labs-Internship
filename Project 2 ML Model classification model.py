"""
Name: Mohammad Zeeshan Mufti 
Decode Labs AI internship Project 2AI: Data Classification Using 
Organization 
Description  :
This project builds a machine learning classification model
using the Iris dataset. The K-Nearest Neighbors (KNN)
algorithm is used to classify flower species based on
their physical characteristics.

Breaking down of the flow:
1. Load the dataset
2. Explore the data
3. Split into training and testing sets
4. Standardize features
5. Train the KNN model
6. Make predictions
7. Evaluate model performance

"""

# Import required libraries
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report,
    f1_score
)

import pandas as pd


def load_dataset():
    """
    Loads the Iris dataset and converts it into
    a Pandas DataFrame for easier analysis.
    """

    # Load the built-in Iris dataset
    iris = load_iris()

    # Convert feature data into a DataFrame
    X = pd.DataFrame(
        iris.data,
        columns=iris.feature_names
    )

    # Store target labels in a Series
    y = pd.Series(
        iris.target,
        name="Species"
    )

    return X, y, iris.target_names


def display_dataset_info(X, y):
    """
    Displays basic information about the dataset.
    """

    print("=" * 60)
    print("IRIS DATASET INFORMATION")
    print("=" * 60)

    # Display dataset dimensions
    print(f"\nNumber of Samples : {X.shape[0]}")
    print(f"Number of Features: {X.shape[1]}")

    # Display feature names
    print("\nFeature Names:")
    for column in X.columns:
        print(f"• {column}")

    # Show first few records
    print("\nFirst Five Records:")
    print(X.head())

    # Display class distribution
    print("\nClass Distribution:")
    print(y.value_counts().sort_index())

    print("=" * 60)


def preprocess_data(X, y):
    """
    Splits the dataset and standardizes
    feature values.
    """

    # Split the dataset into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.20,
        random_state=42,
        stratify=y
    )

    # Create a scaler object
    scaler = StandardScaler()

    # Learn scaling parameters from training data
    X_train_scaled = scaler.fit_transform(X_train)

    # Apply the same scaling to testing data
    X_test_scaled = scaler.transform(X_test)

    return X_train_scaled, X_test_scaled, y_train, y_test


def train_model(X_train, y_train):
    """
    Creates and trains the KNN classifier.
    """

    # Initialize the classifier with K = 5
    classifier = KNeighborsClassifier(n_neighbors=5)

    # Train the model using the training data
    classifier.fit(X_train, y_train)

    return classifier


def evaluate_model(model, X_test, y_test, target_names):
    """
    Evaluates model performance using different metrics.
    """

    # Predict the class labels for unseen data
    predictions = model.predict(X_test)

    # Calculate evaluation metrics
    accuracy = accuracy_score(y_test, predictions)

    f1 = f1_score(
        y_test,
        predictions,
        average="weighted"
    )

    matrix = confusion_matrix(y_test, predictions)

    report = classification_report(
        y_test,
        predictions,
        target_names=target_names
    )

    # Display evaluation results
    print("\nMODEL PERFORMANCE")
    print("=" * 60)

    print(f"Accuracy Score : {accuracy:.2%}")
    print(f"F1 Score       : {f1:.4f}")

    print("\nConfusion Matrix")
    print(matrix)

    print("\nClassification Report")
    print(report)


def main():
    """
    Main function that controls the project workflow.
    """

    try:

        # Step 1: Load dataset
        X, y, target_names = load_dataset()

        # Step 2: Display dataset information
        display_dataset_info(X, y)

        # Step 3: Split and preprocess the data
        X_train, X_test, y_train, y_test = preprocess_data(X, y)

        # Step 4: Train the machine learning model
        model = train_model(X_train, y_train)

        # Step 5: Evaluate model performance
        evaluate_model(
            model,
            X_test,
            y_test,
            target_names
        )

        print("=" * 60)
        print("Project executed successfully.")
        print("=" * 60)

    except Exception as error:
        # Handle unexpected errors gracefully
        print("\nAn unexpected error occurred.")
        print(error)


# Execute the program only if this file is run directly
if __name__ == "__main__":
    main()