# Twitter-Sentiment-Analysis-Bot


## About

This is a twitter-based bot that checks for tweets @botname. It uses the VADER-Sentiment Analysis Library to form an opinion on a tweet, and displays the percentage of negative/positive/neutral tweets toward a specific topic, out of a given number of tweets (the default is 1000). The documentation for VADER can be found here: https://github.com/cjhutto/vaderSentiment . 

As of 12/4/2019, this bot is currently running on https://www.pythonanywhere.com/

## How to Run
In order to run this bot, you must have a Twitter Developer account and have you access tokens. Save your keys in a file called twitter_keys.txt as api_key, api_secret_key, access_token, and access_secret_token.

Then, run the program from your local machine. 

## Usage
After the bot is running, it will repeatedly scan for recent tweets @botname every minute. The name of your bot will depend on what api tokens you use. Once a tweet @ the bot is found, it will only search for tweets if it is in the format "@botname Search for: [query]. Any other tweets in a different format will recieve an error reply with the correct formatting instructions. Once it has determined the search query, it will reply to the original tweet with the results. The bot repeatedly polls for new tweets every 10 seconds.

## Examples

### Success Case:

Twitter User: "@botname Search for: the lakers"

@botname: (replying to Twitter User) 

          "Results for: the lakers
          The tweets for the given topic were: 7.72% negative , 9.31% positive and 82.98% neutral."
          
   
### Error / Invalid Case:

Twitter User: "@botname How's it going?"

@botname: (replying to Twitter User)

          "Unable to find results.
          To analyze the sentiment for a topic, tweet "@TwSeSC1 Search for:" followed by your query.





