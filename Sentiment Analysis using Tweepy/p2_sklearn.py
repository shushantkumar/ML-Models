# # textblob 
# new1=Textblob("random text here")
# new1.tags  returns the type of speech
# new1.words tokenizez the tags
# new1.sentiment.polarity   gives sentiment -1 to 1 from sad to happy

import csv
import tweepy
from textblob import TextBlob

consumer_key= '8LMIGPdNKwPMasLeUIWpVSY15'
consumer_secret= 'MbQGzudmi6qlGaSEap7FdRQSQkEIT2d5nIn20MuUQn209CnON8'

access_token='959668567401615360-8GHTVoWrTCyf0VGUJABZi5gmCWvWYUG'
access_token_secret='zTqWKZLvFEZMkN9GO2fbLN1TPESnbUF8vcEte7iAXWrsw'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

twitter = tweepy.API(auth)

tweets = twitter.search('game of thrones')



with open('p2sentiment.csv', 'w', newline='') as csvfile:
	out = csv.writer(csvfile, delimiter=' ',quotechar='|', quoting=csv.QUOTE_MINIMAL)
	for tweet in tweets:
		print(tweet.text)
		analysis = TextBlob(tweet.text)
		out.writerow(analysis.sentiment)
		#out.write('\n')
		print(analysis.sentiment)
		print("")


#polarity - how positive or negative the tweet is
#subjectivity - how much opininon it is vs how much factual

    	
    	
    	
    	
    	