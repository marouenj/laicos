#!/usr/bin/python3

# https://dev.twitter.com/oauth/application-only

import sys
import json
import requests

# path to config file
credentials_path = '../credentials.json'

# load config file
with open(credentials_path) as credentials_file:
  credentials = json.load(credentials_file)

# keys designation in config file
key = 'consumer_key'
secret = 'consumer_secret'

# validate config file
if key not in credentials or secret not in credentials:
  print('[ERR] Failure to retrieve required keys')
  sys.exit(1)

# request
url = 'https://api.twitter.com/oauth2/token'
auth = (credentials[key], credentials[secret])
data = {'grant_type' : 'client_credentials'}
r = requests.post(url, auth=auth, data=data)

# check response status
if r.status_code is not 200:
  print('[ERR] Failure to acquire access token')
  sys.exit(1)

# convert string to json structure
access_token = json.loads(r.text)

# path to output file 
access_token_path = '../access_token.json'

# open output file (override)
with open(access_token_path, 'w') as access_token_file:
    json.dump(access_token, access_token_file)

print('[INFO] Success')
