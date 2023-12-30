import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from bs4 import BeautifulSoup
from scipy.sparse import hstack, csr_matrix

# Load website source code
try:
    with open('website_source_code.html', 'r', encoding='utf-8') as file:
        website_code = file.read()
except UnicodeDecodeError:
    # Try a different encoding if 'utf-8' fails
    with open('website_source_code.html', 'r', encoding='ISO-8859-1') as file:
        website_code = file.read()

# Use BeautifulSoup to parse HTML
soup = BeautifulSoup(website_code, 'html.parser')

# Extract visible and invisible links
visible_links = [link.get('href') for link in soup.find_all('a', visible=True)]
invisible_links = [link.get('href') for link in soup.find_all('a', visible=False)]

# Load pattern dataset
pattern_data = pd.read_csv('dark.csv')

# Extract features from pattern dataset
vectorizer = TfidfVectorizer()
pattern_features = vectorizer.fit_transform(pattern_data['text'])

# Add a feature for the presence of invisible links in the pattern dataset
pattern_features_with_links = hstack([pattern_features, csr_matrix(pattern_data['text'].apply(lambda x: len(invisible_links) > 0).values.reshape(-1, 1))])

# Create labels for the pattern dataset (1 for dark pattern, 0 for not a dark pattern)
labels = pattern_data['label']

# Extract features from website source code
website_features = vectorizer.transform([website_code])

# Add a feature for the presence of invisible links in the website feature vector
website_features_with_links = hstack([website_features, csr_matrix([len(invisible_links) > 0])])

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(pattern_features_with_links, labels, test_size=0.2, random_state=42)

# Train the model
model = LogisticRegression()
model.fit(X_train, y_train)

# Make predictions on the website source code
website_pred = model.predict(website_features_with_links)

# Print the result
if website_pred[0] == 1:
    print("The website contains a dark pattern.")
else:
    print("The website does not contain a dark pattern.")
