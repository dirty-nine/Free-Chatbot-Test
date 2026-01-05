
# GPT-4 Free API Request
import requests

def chat(query):
    try:
        url = "https://xyris.vercel.app/api/llm-models/openai/gpt-4/"
        headers = {"Content-Type": "application/json"}
        
        response = requests.post(
            url, 
            json={"query": query}, 
            headers=headers
        )
        response.raise_for_status()
        
        return response.json().get("content", "")
    except requests.RequestException as e:
        print(f"API Request Error: {e}")
        return ""
      

chats = [{'role':'system', 'content':"You are a bratty chat bot who appears reluctant to chat with the user, despite always ending up doing so."}]
while True:
    uP = input("Type Here:\n")
    sP = f"[Chat History]\n{str(chats)}\n[User Prompt]\n{uP}"
    response = chat(sP)
    chats.append({'role':'user', 'content':uP})
    chats.append({'role':'system', 'content':response})
    print(response)
    