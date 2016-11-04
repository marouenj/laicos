#!/usr/bin/python3

import sys
import json
import requests
import os.path

# load tweets
with open('./tweets/url_facebook.json', 'r') as tweets_file:
  tweets = json.load(tweets_file)

print (len(tweets['tweets']))
