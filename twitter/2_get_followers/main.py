#!/usr/bin/python3

#https://dev.twitter.com/rest/reference/get/followers/list

import sys
import json
import requests

# path to config file
access_token_path = '../access_token.json'

# load config file
with open(access_token_path) as access_token_file:
  access_token = json.load(access_token_file)

# keys designation in config file
token = 'access_token'

# validate config file
if token not in access_token:
  print('[ERR] Failure to retrieve required keys')
  sys.exit(1)

access_token = access_token[token]

# path to followees file
followees_path = '../people/followees.json'

# load followees file
with open(followees_path) as followees_file:
  followees = json.load(followees_file)

for followee in followees:
  # request
  url = 'https://api.twitter.com/1.1/followers/list.json'
  params = {'screen_name': followee, 'cursor': '-1', 'count': '200', 'skip_status': 'true', 'include_user_entities': 'false' }
  headers= {'Authorization': 'Bearer ' + access_token}
  r = requests.get(url, params=params, headers=headers)

  # check response status
  if r.status_code is not 200:
    print('[ERR] Failure to acquire list of followers')
    sys.exit(1)

  # convert string to json structure
  followers = json.loads(r.text)

  # path to output file
  followee_path = '../people/' + followee + '_followers.json'

  # open output file (override)
  with open(followee_path, 'w') as followee_file:
    json.dump(followers, followee_file)

  print('[INFO] Success')

