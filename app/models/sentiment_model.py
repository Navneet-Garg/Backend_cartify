from transformers import pipeline

# Initialize the sentiment analysis pipeline
classifier = pipeline("sentiment-analysis", framework="tf")

def generate_response(text):
    result = classifier([text])[0]
    sentiment = result['label']
    confidence = result['score']

    if sentiment == "POSITIVE":
        if confidence >= 0.9:
            response = "Thank you so much, come again!"
        elif confidence >= 0.7:
            response = "Great to hear that! We appreciate your support!"
        else:
            response = "Thanks for your feedback!"
    else:  # NEGATIVE sentiment
        if confidence >= 0.9:
            response = "Sorry for the inconvenience, we will correct it. You won't face this again."
        elif confidence >= 0.4:
            response = "We're sorry you didn't have the best experience. Let us know how we can improve!"
        else:
            response = "We sincerely apologize for the issue. We'll ensure it doesn't happen again."

    return {"input": text, "sentiment": sentiment, "confidence": confidence, "response": response} 