from flask import Flask, request
from strava_auth import exchange_code_for_token
from sheets import save_user_token

app = Flask(__name__)

@app.route("/callback")
def callback():
    code = request.args.get("code")
    user_id = request.args.get("state")  # bisa dikirim via Telegram sebagai parameter
    token_data = exchange_code_for_token(code)
    save_user_token(user_id, token_data["access_token"], token_data["refresh_token"])
    return "Strava berhasil terhubung!"
