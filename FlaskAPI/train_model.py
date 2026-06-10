import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.metrics import classification_report, accuracy_score
from imblearn.over_sampling import SMOTE, RandomOverSampler
import warnings
from sklearn.exceptions import UndefinedMetricWarning
import joblib

# Suppress UndefinedMetricWarnings
warnings.filterwarnings('ignore', category=UndefinedMetricWarning)

# Load dataset
data = pd.read_csv('cs.csv')
print("Dataset columns:", data.columns)

# Prepare features and drop non-relevant columns
X = data.drop(columns=['Future Career', 'Student ID', 'Name'])

# Ensure all categorical features are encoded
categorical_cols = ['Gender', 'Major', 'Interested Domain', 'Projects', 'Python', 'SQL', 'Java']
label_encoders = {col: LabelEncoder() for col in categorical_cols}

for col in categorical_cols:
    if col in X.columns:
        X[col] = label_encoders[col].fit_transform(X[col])

# Verify all columns in X are numeric
print("Feature types after encoding:\n", X.dtypes)

# Target variable
y_encoder = LabelEncoder()
y = y_encoder.fit_transform(data['Future Career'])

# Check class distribution before filtering rare classes
print("Class distribution before filtering rare classes:\n", pd.Series(y).value_counts())

# Filter out classes with fewer than 5 samples
rare_classes = pd.Series(y).value_counts()[pd.Series(y).value_counts() < 5].index
print(f"Removing the following rare classes: {rare_classes}")
filtered_indices = ~pd.Series(y).isin(rare_classes)
X = X[filtered_indices]
y = y[filtered_indices]

# Check the class distribution after filtering
print("Class distribution after filtering rare classes:\n", pd.Series(y).value_counts())

# Ensure dataset is not empty and has more than 1 class
if len(X) == 0 or len(pd.Series(y).value_counts()) <= 1:
    print("Not enough classes in the dataset to train a model. Exiting.")
    exit()

# Split dataset into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# Handle class imbalance with SMOTE, fallback to RandomOverSampler if needed
try:
    smote = SMOTE(random_state=42, k_neighbors=2)
    X_resampled, y_resampled = smote.fit_resample(X_train, y_train)
    print("SMOTE applied successfully.")
except ValueError as e:
    print(f"SMOTE failed: {e}")
    print("Falling back to RandomOverSampler.")
    ros = RandomOverSampler(random_state=42)
    X_resampled, y_resampled = ros.fit_resample(X_train, y_train)

print("Resampled class distribution:\n", pd.Series(y_resampled).value_counts())

# Scale features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X_resampled)
X_test_scaled = scaler.transform(X_test)

# Train model
model = RandomForestClassifier(random_state=42)
model.fit(X_scaled, y_resampled)

# Evaluate model on test data
y_pred = model.predict(X_test_scaled)
print("\nClassification Report:\n", classification_report(y_test, y_pred, zero_division=0))
print(f"Model Accuracy: {accuracy_score(y_test, y_pred):.2f}")

joblib.dump(model, 'model.pkl')
print("Model saved as model.pkl")
