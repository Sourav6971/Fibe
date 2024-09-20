# Import necessary libraries
from data import data
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB

# Sample data

# Separate paragraphs and their categories
def category(article):
    paragraphs = [item[0] for item in data]
    categories = [item[1] for item in data]

    # Convert text data into numerical features using CountVectorizer
    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(paragraphs)

    # Split the data into training and test sets
    X_train, _, y_train, _ = train_test_split(X, categories, test_size=0.2, random_state=42)

    # Initialize and train the Naive Bayes classifier
    classifier = MultinomialNB()
    classifier.fit(X_train, y_train)

    # Predict the category of a new paragraph
    new_paragraph = [article]
    new_paragraph_vectorized = vectorizer.transform(new_paragraph)
    predicted_category = classifier.predict(new_paragraph_vectorized)

    print(f"Predicted category: {predicted_category[0]}")
    return (predicted_category)