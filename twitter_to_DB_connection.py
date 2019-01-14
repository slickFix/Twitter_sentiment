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
            
        except Error as e:
            print(e)

if __name__ == "__main__":
    
    credentials_path = '/home/siddharth/workspace-python/Twitter_sentiment/Twitter_credentials.txt'
    
    with open(credentials_path,'r') as f:
        creds = f.readlines()
    
    consumer_key = creds[0].split('=')[1]
    consumer_secret = creds[1].split('=')[1]
    access_token = creds[2].split('=')[1]
    access_token_secret = creds[3].split('=')[1]
    


    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    
    api = tweepy.API(auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)
    
    listener = MyStreamlistener(api = api)
    
    stream = tweepy.Stream(auth, listener = listener)
    
    track = []
    stream.filter(track = track, languages = ['en'])