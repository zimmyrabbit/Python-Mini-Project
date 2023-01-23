import requests
import json

slack_webhook_url = "https://hooks.slack.com/services/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"

def sendSlackWebhook(strText) :
    headers = {
        "Content-type": "application/json"
    }
    data = {
        "text": strText
    }

    res = requests.post(slack_webhook_url, headers=headers, data=json.dumps(data))

    if res.status_code == 200:
        return "ok"
    else:
        return "error"

print(sendSlackWebhook("파이썬에서 보내는 메세지 테스트"))