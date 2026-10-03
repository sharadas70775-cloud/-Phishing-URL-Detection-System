# Phishing URL Detection System

An intelligent system that extracts structural features from an incoming URL and evaluates whether it is legitimate or a potential phishing attempt using a Random Forest Machine Learning classifier.

## Project Structure
- `data/`: Contains the labeled spreadsheet dataset (`Phishing_Legitimate_full.csv`).
- `models/`: Stores the exported machine learning model brain binary file (`phishing_model.pkl`).
- `src/`: Houses the Python source code elements (`feature_extraction.py`, `train_model.py`, `app.py`).

## Installation & Setup Instructions
1. Open your terminal inside the project directory folder.
2. Ensure your virtual environment is turned on and active:
   ```powershell
   .\venv\Scripts\activate
   ```
3. Install all required code package dependencies:
   ```powershell
   pip install pandas numpy scikit-learn tldextract joblib
   ```

## Execution Flow
1. **Train the System Classifier Model**:
   ```powershell
   python src/train_model.py
   ```
2. **Launch the Core Application Live Interface**:
   ```powershell
   python src/app.py
   ```

