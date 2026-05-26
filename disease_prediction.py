import pandas as pd
from sklearn.tree import DecisionTreeClassifier

# Sample healthcare dataset
data = {
    'fever': [1, 1, 0, 0],
    'cough': [1, 0, 1, 0],
    'headache': [1, 1, 0, 1],
    'disease': ['Flu', 'Viral Fever', 'Cold', 'Migraine']
}

# Create dataframe
df = pd.DataFrame(data)

# Features and target
X = df[['fever', 'cough', 'headache']]
y = df['disease']

# Train model
model = DecisionTreeClassifier()
model.fit(X, y)

print("=== AI Healthcare Prediction System ===")

# User input
fever = int(input("Fever? (1=yes, 0=no): "))
cough = int(input("Cough? (1=yes, 0=no): "))
headache = int(input("Headache? (1=yes, 0=no): "))

# Prediction
prediction = model.predict([[fever, cough, headache]])

print("Predicted Disease:", prediction[0])
