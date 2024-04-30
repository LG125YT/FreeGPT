import requests
from datetime import datetime

headers = {"Content-Type":"application/json"}

data = {"messages":[{"role":"system","content":"\nYou are ChatGPT, a large language model trained by OpenAI. You can use markdown to respond to the user's prompt.\nKnowledge cutoff: 2021-09\nCurrent model: gpt-3.5-turbo\nCurrent time: 4/24/2024, 8:58:39 PM\nLatex inline: $x^2$ \nLatex block: $$e=mc^2$$\n\n"}],"stream":False,"model":"gpt-3.5-turbo","temperature":0.5,"presence_penalty":0,"frequency_penalty":0,"top_p":1}

while True:
	prompt = input("> ")
	date = datetime.now().strftime('%m/%d/%y')
	time = datetime.now().strftime('%I:%M:%S %p')
	data['messages'][0]['content'] = f"\nYou are ChatGPT, a large language model trained by OpenAI.\nKnowledge cutoff: 2021-09\nCurrent model: gpt-3.5-turbo\nCurrent time: {date}, {time}\nLatex inline: $x^2$ \nLatex block: $$e=mc^2$$\n\n"
	data['messages'].append({"role":"user","content":prompt})
	e = requests.post("https://vtlchat-g1.vercel.app/api/openai/v1/chat/completions", json=data)
	print(e.json())
	print(e.json()['choices'][0]['message']['content'])

#max tokens: 512000, play around with whatever exists here ig lol
