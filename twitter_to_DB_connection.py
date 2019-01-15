#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 17:27:03 2019

@author: siddharth
"""

import tweepy
import psycopg2 as pg2
import json


class MyStreamlistener(tweepy.StreamListener):
    
    def on_connect(self):
        print("Connected to twitter API")
        
    def on_error(self,status_code):
        if status_code !=200:
            print("error found {}".format(status_code))
            return False
    
    def on_data(self,data):
        try:
            raw_data = json.loads(data)
            print(raw_data)
            
        except Exception as e:
            print(e)

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
    
    #creating streamlistener object
    listener = MyStreamlistener(api = api)
    
    stream = tweepy.Stream(auth, listener = listener)

    stream.sample()