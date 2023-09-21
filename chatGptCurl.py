import requests
gptResponse = requests.post("https://api.openai.com/v1/chat/completions", headers = {"Authorization": f"Bearer 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"}, json = {"model": "gpt-3.5-turbo", "messages": [{"role": "user", "content": "tell me a fun facts"}]})
if gptResponse.status_code == 200:
    print(gptResponse.json())
else:
    print(gptResponse.status_code, gptResponse.text)