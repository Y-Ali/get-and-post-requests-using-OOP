import requests
import json

def post_requestsssss(post_code):
    post_code = post_code
    post_request_to_postcodes = 'https://api.postcodes.io/postcodes/'
    json_body = json.dumps({"postcodes": post_code})
    headers = {'Content-Type': 'application/json'}


    print(json_body)

    post_request_postcodes = requests.post('https://api.postcodes.io/postcodes', headers=headers, data=json_body)

post_requestsssss("E146HS")
