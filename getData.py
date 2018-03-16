#!/usr/bin/python2.7

import tweepy
from tweepy import OAuthHandler
from utils import getEmosentiment, Emotions, Polarity
from vocab import SentiWords
from tweet import Tweet
import sys
"""
Setting up the auth parameters for using the tweepy module on twitter application created with OAuth.
Twitter username - @e_purohit

Example:

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
"""

def getTestdata(search , count=1, emojis = None):
	auth = tweepy.OAuthHandler("VzAcT7Kf0gAiYBwN9CeKQolqk", "oU80dLgLahfNHS0b7pUZv3EC4MeRZ1UHnpMVbluAlLlSYot4Y0")
	auth.set_access_token("810807258149949440-WWflrBW2sY7iruVQLjN70dCcn1BUoCf", "mDG1BDjVEMJO4QEch1bUEjnsWuvbhqHeQVRi4wwveTgB0")

	api = tweepy.API(auth)
	non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)

	#search = "happy"
	itemlimit = count

	for status in tweepy.Cursor(api.search, lang="en", q=search,tweet_mode="extended", since_id=1).items(itemlimit):
	    # process status here
	    # print status.entities["hashtags"]

	    if "retweeted_status" in dir(status):
	    	tweet=status.retweeted_status.full_text
	    else:
	    	tweet=status.full_text
	

	    t1 = Tweet(tweet.translate(non_bmp_map))
	    t1.processTweet(emojis = emojis)
	    t1.printer()
	    
	    return t1
	    


def getTraindata(bpfile = "Datasets/Train/Sentiment Analysis Dataset.csv", mpfile = "Datasets/Train/smileannotationsfinal.csv", mode = "mp" ,emojis = None):
        mpdata = []
        bpdata = []

        if mode == "bp":
                file = mpfile
        else:
                file = bpfile

        fp = open(file, encoding="utf-8",errors="ignore")
        non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)
        i=1
        for line in fp:
                #line1=line.translate(non_bmp_map)
                tokens = line.split(',')
                labels = tokens[2].split('|')
                if labels[0] in Emotions:
                        label = Emotions[labels[0]]
                        t1 = Tweet(tokens[1], label)
                        t1.processTweet(emojis = emojis)
                        #print (t1.text)
                        mpdata.append(t1)
                i=i+1
        print ("Number of data",i)
                #print(mpdata)

        fp.close()
##        token=mpdata.split(',')
##        print(len(token))
       # print(len(mpdata))
        return mpdata
