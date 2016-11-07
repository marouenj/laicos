import json
import os

# base dir for tweets
default_base = './tweets'
default_iput = 'queries.json'

# keys in json file
i = 'id'
q = 'q'

# request params
count = 100

def load_queries(base=default_base, iput=default_iput):
  path = base + '/' + iput

  # open
  with open(path) as queries_file:
    queries = json.load(queries_file)

  for query in queries:
    # validate query
    if i not in query or q not in query:
      print('[ERR] Failure to validate json file')
      sys.exit(1)

  return queries

def init_queries_output_file(queries, base=default_base):
  for query in queries:
    oput = query[i] + '.json'
    path = base + '/' + oput
    if not os.path.exists(path):
      with open(path, 'w') as tweets_file:
        tweets = {'since_id': '0', 'tweets': []}
        json.dump(tweets, tweets_file)
        tweets_file.close()
