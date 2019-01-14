#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 17:27:03 2019

@author: siddharth
"""

import tweepy


credentials_path = '/home/siddharth/workspace-python/Twitter_sentiment/Twitter_credentials.txt'

with open(credentials_path,'r') as f:
    creds = f.readlines()

consumer_key = creds[0].split('=')[1]
consumer_secret = creds[1].split('=')[1]
access_token = creds[2].split('=')[1]
access_token_secret = creds[3].split('=')[1]


