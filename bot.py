import os
import requests

TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

print("▶ bot start")

if not TOKEN or not CHAT_ID:
    print("❌ BOT_TOKEN 或 CHAT_ID 沒有設定")
    exit()

url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

payload = {
    "chat_id": CHAT_ID,
    "text": "🎉 GitHub Actions 測試成功！"
}

r = requests.post(url, data=payload)

print("status code:", r.status_code)
print("response:", r.text)
