import requests

def expand(url):
  r = requests.head(url)
  if 'location' in r.headers:
    return r.headers['location']
  return url
