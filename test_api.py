import requests

url = "http://127.0.0.1:5000/chat"
payload = {
    "query": "When is the exam?",
    "session_id": "test123"
}

response = requests.post(url, json=payload)
print(response.json())
