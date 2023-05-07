import pandas as pd
import numpy as np
from phishing_utils import extract_features
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split


def train_model(X_train, y_train):
    model = RandomForestClassifier()
    model.fit(X_train, y_train)
    return model

def evaluate_model(model, X_test, y_test):
    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)
    return accuracy

def load_data(file_path):
    data = pd.read_csv("phishing_site_urls.csv")
    return data

def preprocess_data(data):
    X = data["URL"].apply(extract_features).tolist()  # Change 'url' to 'URL'
    y = (data["Label"] == "bad").astype(int).values  # Change 'label' to 'Label' and convert 'bad' and 'good' to binary labels
    return X, y
