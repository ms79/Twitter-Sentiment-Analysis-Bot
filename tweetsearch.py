# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 14:05:45 2019

@author: mshen
"""

from twitter_keys import api_key,api_secret_key,access_token,access_secret_token
import tweepy
import string
import time
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


auth = tweepy.OAuthHandler(api_key, api_secret_key)
auth.set_access_token(access_token, access_secret_token)

api = tweepy.API(auth,wait_on_rate_limit=True)


def collect_tweets(query,max_tweets=10):
    
    # Searches twitter for tweets in English that include the query. Returns a 
    # list of strings containing the text from each tweet   
    
    cleaned_tweets = []
    searched_tweets=[status for status in tweepy.Cursor(api.search, 
                                        q=query, lang='en').items(max_tweets)]
    for tweet in searched_tweets:
        cleaned_tweets.append(clean_text(tweet.text))
        
    return cleaned_tweets



def analyze_tweets(tweets):
    
    # Takes in a list of strings. Uses the VADER Sentiment analysis to compute
    # the scores. Calculates a rolling average for each category, and returns
    # the dict of scores.
    
    analyzer = SentimentIntensityAnalyzer()
    scores = {'neg':0.0, 'neu':0.0, 'pos':0.0, 'compound':0.0}
    
    for tweet in tweets:
        vs = analyzer.polarity_scores(tweet)
        
        for key in scores:
            scores[key] += (vs[key] * (100/len(tweets)))
        
    return scores

def clean_text(tweet_text):
    
    # Takes in a string and creates a new string excluding characters that are 
    # not punctuation or letters/numbers. Returns the newly created string.
    
    cleaned_tweet = ''
    
    for letter in tweet_text:
        if letter in string.ascii_letters + string.punctuation + string.digits + ' ':
            cleaned_tweet += letter   
            
    return cleaned_tweet
    
def display_sentiment(scores):
    
    # Takes in the list of scores and prints them in a formatted string.
    
    print('The tweets for the given topic were: {0:.2f}% negative'
          .format(scores['neg']))
    print('The tweets for the given topic were: {0:.2f}% positive'
          .format(scores['pos']))
    print('The tweets for the given topic were: {0:.2f}% neutral'
          .format(scores['neu']))
    print(scores['compound'])
    
    
def scan_tweets(recent_id):
    
    # Search for tweets mentioning the bot after the most recent tweet ID
    
    scores = {};
    query = ""
    
    scanned_tweets=[tweet for tweet in tweepy.Cursor(api.mentions_timeline,
                                  since_id=recent_id).items()]
        
    # If no new tweets are found, then return the old ID value
    if len(scanned_tweets) == 0:
        updated_id = recent_id
        
    # Otherwise, we want to analyze the new term and return the updated ID
    else:    
        for tweet in scanned_tweets:
            reply_user = tweet.user.screen_name
            query = find_query(tweet)
            collected_tweets = collect_tweets(query)
            
            if query != '':   
                scores = analyze_tweets(collected_tweets)
                print(scores)
                status = api.update_status('@'+
                                reply_user+' Results for: ' + query +
                                  '\nThe tweets for the given topic were: '
                                  '{0:.2f}% negative , {1:.2f}% positive '
                                  'and {2:.2f}% neutral.'.format(scores['neg'],
                                    scores['pos'], scores['neu']), 
                                       in_reply_to_status_id=tweet.id)
                updated_id = status.id
            else:
                status = api.update_status('@'+reply_user+
                                           ' Unable to find results.'
                                  '\nTo analyze the sentiment for a topic, '
                                  'tweet "@TwSeSC1 Search for:" followed'
                                  ' by your query.', updated_id)
                updated_id = status.id
                
    return updated_id


def find_query(tweet):
    
    # Determines the search query for the tweet. If the search is not in the 
    # correct format, then an empty string is returned.
    
    if 'Search for:' in tweet.text:
        return tweet.text.replace('@maxshen42 Search for:','')
    else: 
        return ''

def main():
    
    # Finds the most recent tweet from the timeline and uses the ID from that 
    # tweet to search for new tweets. Makes the call to scan_tweets.
    # Continuously searches every 10 seconds for new tweets.
    
    latest_id = api.user_timeline()[0].id
    while(True):
        latest_id = scan_tweets(latest_id)
        
        time.sleep(10)
        
    print('Finished executing')
    return


        
main()



         
