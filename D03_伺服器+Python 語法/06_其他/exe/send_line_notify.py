import requests
import os
from dotenv import load_dotenv

# 載入 .env 文件
load_dotenv()

def send_line_notify(msg):
    # 用自己的 token 替換
    TOKEN = Q1yoEAgiLrqGviBeASDOVGmUYpFoHcehwa1OmNxv2dU 
    LINE_ENDPOINT = "https://notify-api.line.me/api/notify"
    message = msg
    headers = {
        "Authorization": f"Bearer {TOKEN}",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {"message": message}
    response = requests.post(LINE_ENDPOINT, headers=headers, data=data)
    return response.status_code

if __name__ == "__main__":
    send_line_notify("\n 樹莓派已開機")