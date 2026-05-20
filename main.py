import requests 

message = requests.get("http://api.quotable.io/random")
data = message.json()

citation = data ["content"]
auteur = data ["author"]