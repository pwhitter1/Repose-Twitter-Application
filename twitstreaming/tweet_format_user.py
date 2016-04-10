#Grab the usernames only

#import the necessary package to process data in JSON format
try:
   import json
except ImportError:
    import simplejson as json

# We use the file saved from last step as example
tweets_filename = 'message.txt'
tweets_file = open(tweets_filename, "r")

for line in tweets_file:
    try:
        # Read in one line of the file, convert it into a json object
        tweet = json.loads(line.strip())
        if 'text' in tweet: # only messages contains 'text' field is a tweet
		print tweet['user']['screen_name'] # name of the user account, e.g. "cocoweixu"


    except:
        # read in a line is not in JSON format (sometimes error occured)
        continue
