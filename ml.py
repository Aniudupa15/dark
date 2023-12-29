import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Load website source code
with open('website_source_code.html', 'r') as file:
    website_code = file.read()

# Load pattern dataset
pattern_data = pd.read_csv('dark.csv')

# Extract features from pattern dataset
vectorizer = TfidfVectorizer()
pattern_features = vectorizer.fit_transform(pattern_data['text'])

# Create labels for the pattern dataset (1 for dark pattern, 0 for not a dark pattern)
labels = pattern_data['label']

# Extract features from website source code
website_features = vectorizer.transform([website_code])

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(pattern_features, labels, test_size=0.2, random_state=42)

# Train the model
model = LogisticRegression()
model.fit(X_train, y_train)

# Make predictions on the website source code
website_pred = model.predict(website_features)

# Print the result
if website_pred[0] == 1:
    print("The website contains a dark pattern.")
else:
    print("The website does not contain a dark pattern.")
