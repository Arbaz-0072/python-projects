# AIML Experiment 12 - Smart Chatbot using Scikit-learn

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Chatbot responses dataset
corpus = [
    "Hello! How can I help you?",
    "I am a chatbot created for AIML practical.",
    "I can answer your basic questions.",
    "My favorite language is Python.",
    "Goodbye! Have a nice day."
]

# TF-IDF vectorization
vectorizer = TfidfVectorizer()

while True:
    user_input = input("You: ").lower()
    if user_input in ["exit", "bye", "quit"]:
        print("Bot: Goodbye! 👋")
        break

    # Combine user input with the corpus
    all_text = corpus + [user_input]
    tfidf = vectorizer.fit_transform(all_text)

    # Calculate similarity
    similarity = cosine_similarity(tfidf[-1], tfidf[:-1])
    index = similarity.argsort()[0][-1]

    # If similarity is low, give generic reply
    if similarity[0][index] < 0.2:
        print("Bot: Sorry, I didn’t understand that.")
    else:
        print("Bot:", corpus[index])
