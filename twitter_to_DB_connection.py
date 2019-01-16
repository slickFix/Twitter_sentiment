#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 17:27:03 2019

@author: siddharth
"""

import tweepy
import psycopg2 as pg2
import json

from dateutil import parser


def storeTweet(username, created_at, tweet, retweet_count, place, location):

    #connecting and storing the tweets into the timeline_tweets table
    try:
        conn = pg2.connect("dbname='twitterDB' user='postgres' \
                           host='localhost' port='5432' password='postgres'")
        
        print('he')
        if conn.closed == 0:  # checks if connection is active
            cur = conn.cursor()    
            querry = 'INSERT INTO timeline_tweets (username,time_created,tweet,retweet_count,place_tweet,location_user) VALUES (%s, %s, %s, %s, %s, %s)'
            #inserting tweets into the DB
            cur.execute(querry,(username, created_at, tweet, retweet_count, place, location))
            conn.commit()
            
    except Exception as e:
        print(e)
    
    cur.close()
    conn.close()
    
        
if __name__ == "__main__":
    
    
    #setting up the credentials
    credentials_path = '/home/siddharth/workspace-python/Twitter_sentiment/Twitter_credentials.txt'
    with open(credentials_path,'r') as f:
        creds_raw = f.read()
    
    creds = json.loads(creds_raw)
    consumer_key = creds['creds']['consumer_key']
    consumer_secret = creds['creds']['consumer_secret']
    access_token = creds['creds']['access_token']
    access_token_secret = creds['creds']['access_token_secret']
        
    #setting up the authentication
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)
    
    #creating cursor for home timeline browsing 
    
    for status in tweepy.Cursor(api.home_timeline, screen_name='@sidd_shukla08', tweet_mode="extended").items(5):
        val = json.dumps(status._json)
        val_dict = json.loads(val)

        username = val_dict['user']['screen_name']
        created_at = parser.parse(val_dict['created_at'])

        tweet = val_dict['full_text']
        
        retweet_count = val_dict['retweet_count']
            
        if val_dict['place'] is not None:
            place = val_dict['place']['country']
        else:
            place = None
        
        location = val_dict['user']['location']

		#insert data just collected into postgreSQL
        storeTweet(username, created_at, tweet, retweet_count, place, location)
        print(username, created_at, tweet, retweet_count, place, location, sep='*')
        print('---------------')


    
# =============================================================================
#     #testing storeTweet function
#     
#     username = 'whodiniz'
#     created_at = '2019-01-15 13:02:02+00:00'
#     tweet = 'Future confirms Travis Scott and Young Thug for The WIZRD https://t.co/pmp0L1A5Mt #NewMusic #HipHop #rap New Album… https://t.co/cCTO5j0v7U'
#     retweet_count = 0
#     place = None
#     location = 'Mars'
#     
#     storeTweet(username, created_at, tweet, retweet_count, place, location)
# =============================================================================
