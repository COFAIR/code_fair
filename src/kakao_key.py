import requests

url = 'https://kauth.kakao.com/oauth/token'
rest_api_key = '2e8b2179cbbdcfbf4a32144cdd752e72'
redirect_uri = 'https://example.com/oauth'
authorize_code = 'CJprnLR8iYgXemaEZHOirCFfSq7nvzAO0kzJ7xt3L_o55VOwbDJuTVfZqCsKPXWcAAABjrHMD3FAPV-WDrAHcw'

data = {
    'grant_type':'authorization_code',
    'client_id':rest_api_key,
    'redirect_uri':redirect_uri,
    'code': authorize_code,
    }

response = requests.post(url, data=data)
tokens = response.json()
print(tokens)

# json 저장
import json
#1.
with open(r"C:\코드페어\code_fair\src\kakao_code.json","w") as fp:
    json.dump(tokens, fp)