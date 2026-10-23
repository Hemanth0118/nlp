text = input("Enter a sentence: ").lower()

positive = ["good", "great", "happy", "love", "excellent", "awesome"]
negative = ["bad", "sad", "hate", "worst", "terrible", "poor"]

pos = sum(word in text.split() for word in positive)
neg = sum(word in text.split() for word in negative)

if pos > neg:
    print("Sentiment: Positive 😊")
elif neg > pos:
    print("Sentiment: Negative 😞")
else:
    print("Sentiment: Neutral 😐")