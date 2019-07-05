# Twitter_sentiment

This repository is an attempt to build the twitter tweet (general tweets and from the personal user timeline tweets) storage pipeline.

Also it uses "TextBlob" library to understand the tweet's sentiment and builds a "tag cloud" from the tweet corpus.

### Files description
* twitter_to_DB_connection.py 
  * Python file to retreive tweets either from general tweet api or from the personal account home timeline( asks user for option). For whichever option selected it stores the tweet in PostgreSQL database.
    
    It captures following parameters for the general tweets:
      * Username
      * Time_created
      * Tweet
      * Retweet_count
      * Place_of_tweet
      * Default_location_of_user
      
* Tweet_sentiments.ipynb
  * Jupyter notebook which loads data from the PSQL DB. Cleans tweet, calculates sentiment and builds tag cloud.
