import gspread
from oauth2client.service_account import ServiceAccountCredentials

def get_sheet():
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
    client = gspread.authorize(creds)
    return client.open("StravaBotData").sheet1

def save_user_token(user_id, access_token, refresh_token):
    sheet = get_sheet()
    sheet.append_row([str(user_id), access_token, refresh_token])
