import requests
import json
import fake_useragent

conversation = []
ua = fake_useragent.UserAgent(browsers=['chrome', "firefox", "opera", "safari", "edge", "internet explorer"])
headers = {'Origin': 'https://chat.ramxn.dev',
           'Referer': 'https://chat.ramxn.dev/chat/',
           'content-type': 'application/json', #unless specifically defined, attempting to send POST requests will return a 415 response
           'accept': 'text/event-stream',
           'user-agent': ua.random} #some of these headers are probably unnecessary, I just added them here for good measure

while True:
    content = input("You: ")
    conversation.append({"role": "user", "content": content})
    data = json.dumps({"api_key":"",
        "conversation_id":"3130d075-9664-33ee-adef-189fa74cfc9",
        "action":"_ask",
        "model":"oasst-sft-6-llama-30b", #different models available, available models listed in the README.md file
        "jailbreak":"default",
        "meta":
            {#"id":"7267617785132685338", #possibly unnecessary
            "content":
                {"conversation":conversation,
                "internet_access":False,
                "content_type":"text",
                "parts":
                [{"content":content,"role":"user"}]
                }
            }
        })

    response = requests.post(url="https://chat.ramxn.dev/backend-api/v2/conversation",headers=headers,data=data)

    print(f"GPT:{response.text}")
    conversation.append({"role": "assistant", "content": response.text})
