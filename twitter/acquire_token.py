#!/usr/bin/python3

# https://dev.twitter.com/oauth/application-only

import sys
import json
import requests

# keys in json file
key = 'consumer_key'
secret = 'consumer_secret'

def load_credentials(path):
  # load
  with open(path) as credentials_file:
    credentials = json.load(credentials_file)

  # validate
  if key not in credentials or secret not in credentials:
    print('[ERR] Failure to retrieve required keys')
    sys.exit(1)

  return credentials

# load
credentials = load_credentials('./credentials/credentials.json')

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

# delete unnecessary keys
del access_token['token_type']

# open output file (override)
with open('./credentials/access_token.json', 'w') as access_token_file:
    json.dump(access_token, access_token_file)

print('[INFO] Success')
