# 官方文件

_以下是 LINE Notify API 的[官方文件](https://notify-bot.line.me/doc/en/)重點說明，並搭配 Python 實作完整的 OAuth 認證流程，_

<br>

## 說明

_以下分作四個範例說明 OAuth2 驗證流程_

1. 生成 OAuth2 URL：透過OAuth2進行授權和獲取訪問令牌。

<br>

2. 訪問令牌：使用者需要同意授權應用程式訪問他們的 `LINE Notify` 資源，授權成功後，`LINE Notify` 會將使用者重定向到應用程式指定的 `redirect_uri`，並附帶一個 `授權碼（authorization code）`，接著應用程式會使用該 `授權碼` 向 `LINE Notify` 的 `令牌端點（token endpoint）` 請求 `訪問令牌（access token）`，獲得訪問令牌後，應用程式可以使用該令牌發送 LINE Notify 通知。

<br>

3. 發送通知：使用獲取的訪問令牌發送通知，支持文字、圖片和貼圖等。

<br>

4. 檢查連線狀態：檢查訪問令牌的有效性，並獲取用戶或群組資訊。

<br>

5. 撤銷通知設定：撤銷訪問令牌，終止通知服務。

<br>

## OAuth2 驗證流程

1. 生成 OAuth2 URL：用來讓使用者進行 LINE Notify 的 OAuth2 授權。

```python
import requests
from urllib.parse import urlencode

def generate_oauth_url(client_id, redirect_uri, state):
    base_url = "https://notify-bot.line.me/oauth/authorize"
    params = {
        "response_type": "code",
        # LINE Notify 客戶端 ID
        "client_id": client_id,
        "redirect_uri": redirect_uri,
        "scope": "notify",
        "state": state,
        "response_mode": "form_post"
    }
    return f"{base_url}?{urlencode(params)}"

client_id = "YOUR_CLIENT_ID"
redirect_uri = "YOUR_REDIRECT_URI"
state = "YOUR_STATE"
oauth_url = generate_oauth_url(client_id, redirect_uri, state)
#  輸出 URL
print(oauth_url)
```

<br>

2. OAuth2 訪問令牌

```python
def get_access_token(client_id, client_secret, code, redirect_uri):
    url = "https://notify-bot.line.me/oauth/token"
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    data = {
        "grant_type": "authorization_code",
        "code": code,
        "redirect_uri": redirect_uri,
        "client_id": client_id,
        "client_secret": client_secret
    }
    response = requests.post(url, headers=headers, data=data)
    return response.json()

client_id = "YOUR_CLIENT_ID"
client_secret = "YOUR_CLIENT_SECRET"
code = "AUTHORIZATION_CODE"
redirect_uri = "YOUR_REDIRECT_URI"
token_response = get_access_token(
    client_id, client_secret, code, redirect_uri
)
print(token_response)
```

<br>

3. 發送通知

```python
def send_line_notify(access_token, message, image_thumbnail=None, image_fullsize=None, image_file=None, sticker_package_id=None, sticker_id=None, notification_disabled=False):
    url = "https://notify-api.line.me/api/notify"
    headers = {
        "Authorization": f"Bearer {access_token}"
    }
    data = {
        "message": message,
        "notificationDisabled": notification_disabled
    }
    files = {}
    if image_thumbnail:
        data["imageThumbnail"] = image_thumbnail
    if image_fullsize:
        data["imageFullsize"] = image_fullsize
    if image_file:
        files["imageFile"] = open(image_file, 'rb')
    if sticker_package_id and sticker_id:
        data["stickerPackageId"] = sticker_package_id
        data["stickerId"] = sticker_id

    response = requests.post(url, headers=headers, data=data, files=files)
    return response.json()

access_token = "YOUR_ACCESS_TOKEN"
message = "Hello, this is a test message!"
response = send_line_notify(access_token, message)
print(response)
```

<br>

4. 檢查連線狀態

```python
def check_status(access_token):
    url = "https://notify-api.line.me/api/status"
    headers = {
        "Authorization": f"Bearer {access_token}"
    }
    response = requests.get(url, headers=headers)
    return response.json()

access_token = "YOUR_ACCESS_TOKEN"
status_response = check_status(access_token)
print(status_response)
```

<br>

5. 撤銷通知設定

```python
def revoke_access_token(access_token):
    url = "https://notify-api.line.me/api/revoke"
    headers = {
        "Authorization": f"Bearer {access_token}"
    }
    response = requests.post(url, headers=headers)
    return response.json()

access_token = "YOUR_ACCESS_TOKEN"
revoke_response = revoke_access_token(access_token)
print(revoke_response)
```

<br>
