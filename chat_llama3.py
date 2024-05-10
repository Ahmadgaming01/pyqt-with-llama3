import ollama


input_text = 'hello'
stream = ollama.chat(
    model='llama3',
    messages=[{'role': 'user', 'content': input_text}],
    stream=True,
)


for chunk in stream:
    print(chunk['message']['content'], end='', flush=True)





