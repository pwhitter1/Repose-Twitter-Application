#Just to test the class

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

#retrieves the most X mentions of the keyword Y
#the above is what is supposed to happen, but what seems to be happening is that it searches until it finds one match...
#which is better than the previous tactic I used where the program would time out in a manner of seconds 
twts = [status for status in tweepy.Cursor(api.search, q="Hello!").items(20)]     
 
#list of specific strings we want to check for in Tweets
t = ['Hello!',
    'Hello',
    'hello!',
    'hello']
 
for s in twts:
    for i in t:
        if i == s.text:
            sn = s.user.screen_name
            m = "@%s Please ignore. This is a test." % (sn)
            s = api.update_status(m, s.id)
