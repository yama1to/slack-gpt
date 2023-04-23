### Yamato Sakino ###

import os
import openai
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

# 環境変数から認証情報を取得
SLACK_APP_TOKEN = os.environ.get("SLACK_APP_TOKEN")
SLACK_BOT_TOKEN = os.environ.get("SLACK_BOT_TOKEN")
SLACK_SIGNING_SECRET = os.environ.get("SLACK_SIGNING_SECRET")

openai.api_key = os.environ.get("OPENAI")

def get_answer(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=3000,
        n=1,
        stop=None,
        temperature=0.5,
    )
    message = response.choices[0].text.strip()
    return message

app = App(token=SLACK_BOT_TOKEN, signing_secret=SLACK_SIGNING_SECRET)

# メンションに対するリスナー
@app.event("app_mention")
def command_handler(body, say):
    print("Mention RUN")
    text = body['event'].get('text')
    try:
        ans = get_answer(text)
    except Exception as e:
        print(e)
    say(ans)

# message.channelsイベントに対するリスナー
@app.event("message")
def handle_message(body, logger):
    print("Message RUN")
    data = body.get("event")
    # ボット自身のメッセージを無視
    if data.get("subtype") == "bot_message":
        return

    # メッセージを取得し、適切な応答を返すコードを記述
    text = ""
    text += data.get("text")
    channel_id = data.get("channel")
    try:
        response = get_answer(text)
    except Exception as e:
        print(e)

    # 返信をチャンネルに送信
    try:
        app.client.chat_postMessage(channel=channel_id, text=response)
    except Exception as e:
        logger.error(f"Error posting message: {e}")

# Socket Modeを使用してリスナーを起動
try:
    handler = SocketModeHandler(app, SLACK_APP_TOKEN)
    handler.start()

except Exception as e:
    print(e)


