#!/usr/bin/python3

# https://dev.twitter.com/rest/public/search
# https://dev.twitter.com/rest/reference/get/search/tweets

import sys
import json
import requests
import os.path

import my_auth
import my_query

from my_query import default_base, default_iput, i, q, count

# load access token
access_token = my_auth.load_access_token()

# load queries
queries = my_query.load_queries()
my_query.init_queries_output_file(queries)

# execute each query
for query in queries:
  path = default_base + '/' + query[i] + '.json'

  # load previously saved tweets from the same query
  with open(path, 'r+') as tweets_file:
    tweets = json.load(tweets_file)

  # request
  url = 'https://api.twitter.com/1.1/search/tweets.json'
  params = {'q': query[q], 'result_type': 'recent', 'count': count, 'since_id': tweets['since_id']}
  headers= {'Authorization': 'Bearer ' + access_token}
  r = requests.get(url, params=params, headers=headers)

  # check response status
  if r.status_code is 429:
    print('[WARN] Too many request')
    sys.exit(429)
  if r.status_code is not 200:
    print('[ERR] Failure to get tweets')
    print(r.status_code)
    print(r.text)
    sys.exit(1)

  # convert string to json structure
  new_tweets = json.loads(r.text)
  print(len(new_tweets['statuses']))

  # update since_id
  tweets['since_id'] = new_tweets['search_metadata']['max_id_str']

  # append list of tweets
  tweets['tweets'].extend(new_tweets['statuses'])

  with open(path, 'w') as tweets_file:
    json.dump(tweets, tweets_file)

print('[INFO] Success')
