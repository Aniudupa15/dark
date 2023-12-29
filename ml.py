import pandas as pd
# Load website source code
with open('website_source_code.html', 'r') as file:
    website_code = file.read()
# Load pattern dataset
pattern_data = pd.read_csv('pattern.csv')
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
# Extract features from website source code
vectorizer = TfidfVectorizer()
website_features = vectorizer.fit_transform([website_code])
# Extract features from pattern dataset
pattern_features = vectorizer.transform(pattern_data['pattern_text'])
# Create labels for the pattern dataset (1 for dark pattern, 0 for not a dark pattern)
labels = pattern_data['is_dark_pattern']
from sklearn.linear_model import LogisticRegression
# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(pattern_features, labels, test_size=0.2, random_state=42)
# Train the model
model = LogisticRegression()
model.fit(X_train, y_train)
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
# Make predictions
y_pred = model.predict(X_test)
# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)
classification_rep = classification_report(y_test, y_pred)
print(f'Accuracy: {accuracy}')
print(f'Confusion Matrix:\n{conf_matrix}')
print(f'Classification Report:\n{classification_rep}')
