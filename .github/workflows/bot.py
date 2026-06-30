import os
import requests

# 從 GitHub Secrets 讀資料
TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

print("▶ bot start")
print("TOKEN exists:", bool(TOKEN))
print("CHAT_ID:", CHAT_ID)

# 檢查有沒有讀到（避免白跑）
if not TOKEN or not CHAT_ID:
    print("❌ 沒讀到 BOT_TOKEN 或 CHAT_ID，請檢查 GitHub Secrets")
    exit()

# Telegram API
url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

payload = {
    "chat_id": CHAT_ID,
    "text": "🔥 GitHub Bot 測試成功！"
}

# 發送訊息
r = requests.post(url, data=payload)

print("status code:", r.status_code)
print("response:", r.text)
