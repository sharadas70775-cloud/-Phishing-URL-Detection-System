import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import joblib
import os

# 1. Load your dataset from the data folder
data_path = os.path.join('data', 'Phishing_Legitimate_full.csv')
print("Loading dataset from:", data_path)
df = pd.read_csv(data_path)

# Import the feature extraction logic
from feature_extraction import extract_features

# Let's inspect column names dynamically to prevent header errors
print("Detected Dataset Columns:", list(df.columns))

# Find the URL column name dynamically
url_column = None
for col in df.columns:
    if 'url' in col.lower():
        url_column = col
        break

# Find the Label column name dynamically 
label_column = None
for col in df.columns:
    if 'label' in col.lower() or 'result' in col.lower() or 'status' in col.lower():
        label_column = col
        break

if not url_column or not label_column:
    raise ValueError(f"Could not automatically map columns! Found columns: {list(df.columns)}")

print(f"Using '{url_column}' for Web Addresses and '{label_column}' for Target Classification Labels.")
print("Extracting structural features from URLs... This might take a moment...")

# 2. Extract features loop
feature_list = []
for index, row in df.iterrows():
    url_string = row[url_column]
    extracted = extract_features(str(url_string))
    feature_list.append(extracted)

# Clean structured feature table matrix
X = pd.DataFrame(feature_list)
y = df[label_column]

# 3. Data Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print("Training Machine Learning Model (Random Forest Classifier)...")
# 4. Train
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# 5. Save the trained brain file
model_output_path = os.path.join('models', 'phishing_model.pkl')
joblib.dump(model, model_output_path)
print(f"Model successfully saved to: {model_output_path}")

# 6. Evaluation metrics metrics
y_pred = model.predict(X_test)

print("\n=== PROJECT EVALUATION METRICS ===")
print("Accuracy Score:", accuracy_score(y_test, y_pred))
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

