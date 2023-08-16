# FreeGPT
Connections to free ChatGPT-like websites so you dont have to pay for an OpenAI API key.

## How to Use:
Pretty simple, just download and run the code. Everything is already set up, however be warned that this isn't perfect. While conducting some tests I have noticed that the AI doesn't always recognize chat history correctly, so if you have any fixes, please create a pull request.

## Available Models:
If you noticed the comment in Line 19, then you probably are here for the different GPT/LLaMa models that the website provides. Here they are (Note that some might not work or have a strict ratelimit):
### GPT:
- `gpt-3.5-turbo`
- `gpt-3.5-turbo-0301`
- `gpt-3.5-turbo-16k`
- `gpt-4`
- `gpt-4-0314`
- `gpt-4-32k`
### LLAMA:
- `oasst-sft-6-llama-30b`
- `llama-2-70b-chat`

You can switch through any of these models to your preference, however, I prefer the one that is in `main.py` because I recieved the least ratelimits when testing it out.
