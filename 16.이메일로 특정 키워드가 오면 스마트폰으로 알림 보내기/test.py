# https://kauth.kakao.com/oauth/authorize?client_id=f563a35321798bd1ad4ab138fec44b92&redirect_uri=https://example.com/oauth&response_type=code

import requests
import json

url = 'https://kauth.kakao.com/oauth/authorize?client_id=f563a35321798bd1ad4ab138fec44b92&redirect_uri=https://example.com/oauth&response_type=code'

response = requests.post(url)

print(response.url)