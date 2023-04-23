# slack-gpt

SlackにOPENAIのGPT3.5をBotとして導入します。
1. ./setup.sh
2. Slackの設定を行なってください。
    Slackアプリの作成
    Slackのアプリを作成し、Botトークンとアプリトークンを取得する必要があります。また、アプリトークンのOAuthスコープにはapp_mentions:readとchat:writeを追加する必要があります。
    Socket Modeの有効化
    Socket Modeを使用する場合は、Slackアプリの設定でSocket Modeを有効にする必要があります。Socket Modeを有効にするには、以下の手順を実行します。
    アプリの「App Home」セクションに移動します。
    「Add features and functionality」ボタンをクリックして、Socket Modeを有効にします。
    Socket Modeを有効にするための設定を入力します。
3. python3 gpt.py
