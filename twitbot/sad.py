#!/usr/bin/env python
import tweepy
#from our keys module (keys.py), import the keys dictionary
from keys import keys
 
CONSUMER_KEY = keys['consumer_key']
CONSUMER_SECRET = keys['consumer_secret']
ACCESS_TOKEN = keys['access_token']
ACCESS_TOKEN_SECRET = keys['access_token_secret']
 
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)
  
#twts = api.search(q="I feel", count = 10) 

#retrieves the most X mentions of the keyword Y
#the above is what is supposed to happen, but what seems to be happening is that it searches until it finds one match...
#which is better than the previous tactic I used where the program would time out in a manner of seconds
#nvm this is not true either - for the sad keywords it's qitting before returning

twts = [status for status in tweepy.Cursor(api.search, q="I feel").items(1)]   
 
#list of specific strings we want to check for in Tweets
t = ['i feel unwanted', 'I feel unwanted',
     'i feel lonely', 'I feel lonely',
     'i feel depressed', 'I feel depressed',
     'i feel worthless', 'I feel worthless',
     'i feel useless', 'I feel useless']
 
for s in twts:
    for i in t:
        if i == s.text:
            sn = s.user.screen_name
            m = "@%s Hey. You are an amazing person and do not for one second ever think otherwise. I believe in you." % (sn)
            s = api.update_status(m, s.id)
