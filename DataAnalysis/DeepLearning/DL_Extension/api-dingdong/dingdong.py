import os
import json
import slack_sdk
import requests


def load_secret(name, key_path="/Users/jung_yujin_1/workspace/TIL/DataAnalysis/DeepLearning/DL_Extension/api-dingdong"):
    with open(os.path.join(key_path, "./secret.json"), "r") as f:
        secret = json.load(f)[name]
    return secret


class SlackMessenger:
    def __init__(self):
        name = "DINGDONG"
        secret = load_secret(name)
        self.channel = secret["CHANNEL"]
        self.token = secret["ACCESSED_TOKEN"]
        self.web_hook_url = secret["WEB_HOOK_URL"]
        self.client = slack_sdk.WebClient(token=self.token)

    def alarm_msg(self, title, alarm_text, colour="#0000ff"):
        slack_text = make_alarm_format(title, alarm_text, colour)
        response = requests.post(self.web_hook_url, data=slack_text, headers={'Content-Type': 'application/json'})
        if response.status_code != 200:
            raise ValueError(response.status_code, response.text)

def make_alarm_format(title: str, text: str, colour):
    result = {"attachments": [
        {
            "color": colour,
            "blocks": [
                {
                    "type": "section",
                    "text": {
                        "type": "plain_text",
                        "text": f"{title}"
                    }
                },
                {
                    "type": "section",
                    "fields": [
                        {
                            "type": "plain_text",
                            "text": f"{text}"
                        }
                    ]
                }
            ]}]}
    return json.dumps(result)