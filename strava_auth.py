import requests

def exchange_code_for_token(code):
    response = requests.post("https://www.strava.com/oauth/token", data={
        "client_id": "YOUR_CLIENT_ID",
        "client_secret": "YOUR_CLIENT_SECRET",
        "code": code,
        "grant_type": "authorization_code"
    })
    return response.json()
