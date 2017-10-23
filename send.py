# Install deps with: pip install requests_oauthlib
from requests_oauthlib import OAuth1Session
key = 'OCDRQ_7LZDZAx5yLPbZVIiR3'
secret = 'hv1JUEmsvd-Htm*wbSvIm.ok6szD@P.95qJZ%D-k'
gwapi = OAuth1Session(key, client_secret=secret)
req = {
    'sender': 'ExampleSMS',
    'message': 'Hello World',
    'recipients': [{'msisdn': +40726758017}],
}
res = gwapi.post('https://gatewayapi.com/rest/mtsms', json=req)
res.raise_for_status()