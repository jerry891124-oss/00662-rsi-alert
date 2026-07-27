import os
import requests
from datetime import datetime

# LINE 設定
LINE_TOKEN = os.environ.get("LINE_CHANNEL_ACCESS_TOKEN", "").strip()
LINE_USER_ID = os.environ.get("LINE_USER_ID", "").strip()


def send_line(message):
    url = "https://api.line.me/v2/bot/message/push"

    headers = {
        "Authorization": f"Bearer {LINE_TOKEN}",
        "Content-Type": "application/json"
    }

    data = {
        "to": LINE_USER_ID,
        "messages": [
            {
                "type": "text",
                "text": message
            }
        ]
    }

    requests.post(url, headers=headers, json=data)


def main():

    # 測試通知
    message = f"""
🔔 00662 RSI Alert 測試

時間：
{datetime.now()}

系統已連線。
"""

    send_line(message)


if __name__ == "__main__":
    main()
