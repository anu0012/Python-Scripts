import tweepy
from textblob import TextBlob

def get_tweet_sentiment(polarity):
	if polarity > 0:
		return 'positive'
	elif polarity == 0:
		return 'neutral'
	elif polarity < 0:
		return 'negative'

consumer_key = ''   # PUT YOUR CONSUMER KEY
consumer_secret = '' # PUT YOUR CONSUMER SECRET

access_token = '' # PUT YOUR ACCESS TOKEN
access_token_secret = '' # PUT YOUR ACCESS TOKEN SECRET

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

tweets_category = {'positive':[],'neutral':[],'negative':[]}

public_tweets = api.search(q='snapchat',rpp=100)

for tweet in public_tweets:
	#print (tweet.text)
	analysis = TextBlob(tweet.text)
	tweets_category.get(get_tweet_sentiment(analysis.sentiment.polarity)).append(tweet.text)
	#print (analysis.sentiment)

print ('Percentage of positive tweets: ' + str(100*len(tweets_category.get('positive'))/len(public_tweets)) + '%')
print ('Percentage of negative tweets: ' + str(100*len(tweets_category.get('negative'))/len(public_tweets)) + '%')

print ('\n\nPositive tweets are:')
for tweet in tweets_category.get('positive'):
	print (tweet)

print ('\n\nNegative tweets are:')
for tweet in tweets_category.get('negative'):
	print (tweet)

