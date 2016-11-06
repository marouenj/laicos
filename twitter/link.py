#!/usr/bin/python3

import json
import re
import jellyfish

import myurl

# load tweets
with open('./tweets/url_facebook.json', 'r') as tweets_file:
  tweets = json.load(tweets_file)

# for each tweet
i = 0
for tweet in tweets['tweets']:
  i+=1
  if len(tweet['entities']['urls']) == 1:
    user = tweet['user']
    name = user['name']
    screen_name = user['screen_name']
    url = tweet['entities']['urls'][0]
    expanded_url = url['expanded_url']
    expanded_url = myurl.expand(expanded_url)
    url_match = re.match('^.*www.facebook.com/(.*)/posts/.*$', expanded_url)
    if url_match:
      fb_name = url_match.group(1)
      print(i)
      print(name.encode('utf-8'))
      print(screen_name)
      print(expanded_url.encode('utf-8'))
      print(fb_name)
      print(jellyfish.jaro_distance(screen_name, fb_name))
      print('')
