import json

access_token_key = 'access_token'

def load_access_token(path='./credentials/access_token.json'):
  # open
  with open(path) as access_token_file:
    access_token = json.load(access_token_file)

  # validate
  if access_token_key not in access_token:
    print('[ERR] Failure to validate json file')
    sys.exit(1)

  return access_token[access_token_key]
