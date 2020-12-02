import time
import requests


def slacksend(title, message):
    url = "https://hooks.slack.com/services/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"
    #message = ("A Sample Message")
    #title = (f"New Incoming Message :zap:")
    slack_data = {
        "username": "NotificationBot",
        "icon_emoji": ":satellite:",
        #"channel" : "#somerandomcahnnel",
        "attachments": [
            {
                "color": "#9733EE",
                "fields": [
                    {
                        "title": title,
                        "value": message,
                        "short": "false",
                    }
                ]
            }
        ]
    }
    #byte_length = str(sys.getsizeof(slack_data))
    headers = {'Content-Type': "application/json"}
    response = requests.post(url, data=json.dumps(slack_data), headers=headers)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)


slacksend("Hi","hi")
