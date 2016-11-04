#!/usr/bin/python3

# https://dev.twitter.com/rest/public/search
# https://dev.twitter.com/rest/reference/get/search/tweets

import sys
import json
import requests
import os.path

# keys in json file
i = 'id'
q = 'q'

def load_access_token():
  # open
  with open('./credentials/access_token.json') as access_token_file:
    access_token = json.load(access_token_file)

  # key in json file
  key = 'access_token'
  
  # validate
  if key not in access_token:
    print('[ERR] Failure to retrieve required keys')
    sys.exit(1)

  return access_token[key]

def load_queries():
  # open
  with open('./tweets/queries.json') as queries_file:
    queries = json.load(queries_file)

  # validate queries
  for query in queries:
    # validate query
    if i not in query or q not in query:
      print('[ERR] Failure to retrieve required keys')
      sys.exit(1)

    # validate output
    path = './tweets/' + query[i] + '.json'
    if not os.path.exists(path):
      with open(path, 'w') as tweets_file:
        tweets = {'since_id': '0', 'tweets': []}
        json.dump(tweets, tweets_file)
        tweets_file.close()

  return queries

# load access token
access_token = load_access_token()

# load queries
queries = load_queries()

# execute each query
for query in queries:
  # load previously saved tweets from the same query
  with open('./tweets/' + query[i] + '.json', 'r+') as tweets_file:
    tweets = json.load(tweets_file)

  # request
  url = 'https://api.twitter.com/1.1/search/tweets.json'
  params = {'q': query[q], 'result_type': 'recent', 'count': '1', 'since_id': tweets['since_id']}
  headers= {'Authorization': 'Bearer ' + access_token}
  r = requests.get(url, params=params, headers=headers)

  # check response status
  if r.status_code is 429:
    print('[WARN] Too many request')
    sys.exit(429)
  if r.status_code is not 200:
    print('[ERR] Failure to acquire list of followers')
    print(r.status_code)
    print(r.text)
    sys.exit(1)

  print(r.text)

  # convert string to json structure
  new_tweets = json.loads(r.text)
  print(len(new_tweets['statuses']))

  # update since_id
  tweets['since_id'] = new_tweets['search_metadata']['max_id_str']

  # append list of tweets
  tweets['tweets'].extend(new_tweets['statuses'])

  with open('./tweets/' + query[i] + '.json', 'w') as tweets_file:
    json.dump(tweets, tweets_file)

  # path to output file
  #followee_path = '../people/' + followee + '_followers.json'

  # open output file (override)
  #with open(followee_path, 'w') as followee_file:
    #json.dump(followers, followee_file)

print('[INFO] Success')
