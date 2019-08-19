# Twitter-Sentiment-Analysis-Bot


## About

This is a twitter-based bot that checks for tweets @botname. It uses the VADER-Sentiment Analysis Library to form an opinion on a tweet, and displays the percentage of negative/positive/neutral tweets toward a specific topic, out of a given number of tweets (the default is 1000). The documentation for VADER can be found here: https://github.com/cjhutto/vaderSentiment . In its current state, the bot is meant to be run on your local machine. I am planning on finding a way to host my bot and to keep it online. 

## How to Run
In order to run this bot, you must have a Twitter Developer account and have you access tokens. Save your keys in a file called twitter_keys.txt as api_key, api_secret_key, access_token, and access_secret_token.

Then, run the program from your local machine. 

## Usage
After the bot is running, it will repeatedly scan for recent tweets @botname every minute. The name of your bot will depend on what api tokens you use. Once a tweet @ the bot is found, it will only search for tweets if it is in the format "@botname Search for: [query]. Any other tweets will be ignored. Once it has determined the search query, it will reply to the original tweet with the results.

## Examples

Twitter User: "@botname Search for: the lakers"

@botname: (replying to Twitter User) 

          "Results for: the lakers
          The tweets for the given topic were: 7.72% negative , 9.31% positive and 82.98% neutral."
          
        






