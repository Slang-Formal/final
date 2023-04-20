from textblob import TextBlob

def sentiment_analysis(sentence):
    # create a TextBlob object and get its sentiment score
    sentiment_score = TextBlob(sentence).sentiment.polarity
    
    # determine sentiment based on score
    if sentiment_score > 0.3:
        return 'Positive'
    elif sentiment_score <-0.3:
        return 'Negative'
    else:
        return 'Neutral'
    
