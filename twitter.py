import oauth2

#consumer_key = 'fckFfzJsrSrRU1St85OXUoRTZ'
#consumer_secret = 'akTOhkghSO9i7pnZ1zXXka5E0Qk8YPE58RStEhtRuBUHde5idn'

def oauth_req(url, key, secret, http_method="GET", post_body="", http_headers=None):
    consumer = oauth2.Consumer(key=key, secret=secret)
    token = oauth2.Token(key=key, secret=secret)
    client = oauth2.Client(consumer, token)
    resp, content = client.request( url, method=http_method, body=post_body, headers=http_headers )
    return content

home_timeline = oauth_req( 'https://api.twitter.com/1.1/statuses/home_timeline.json', "fckFfzJsrSrRU1St85OXUoRTZ", "akTOhkghSO9i7pnZ1zXXka5E0Qk8YPE58RStEhtRuBUHde5idn" )
print(home_timeline)

#data = api.search(q="broadbalk")

#with open('broadbalk.json', 'w') as outfile:
#    json.dump(data[0], outfile)

