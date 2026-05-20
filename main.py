<<<<<<< HEAD
# 2: Génération du HTML
html = f"""<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <title>Citation du jour</title>
    <style>
        body {{
            font-family: Georgia, serif;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            background: #f0f4f8;
        }}
        .card {{
            background: white;
            border-radius: 12px;
            padding: 40px;
            max-width: 600px;
            box-shadow: 0 4px 20px rgba(0,0,0,0.1);
            text-align: center;
        }}
        blockquote {{
            font-size: 1.4em;
            color: #333;
            font-style: italic;
            margin: 0 0 20px 0;
            line-height: 1.6;
        }}
        cite {{
            font-size: 1em;
            color: #888;
        }}
    </style>
</head>
<body>
    <div class="card">
        <blockquote>""</blockquote>
        <cite>— </cite>
    </div>
    
</body>
</html>"""

# 3: Écriture du fichier HTML
fichier = "index.html"
with open(fichier, "w", encoding="utf-8") as f:
    f.write(html)
=======
import requests 

message = requests.get("http://api.quotable.io/random")
data = message.json()

citation = data ["content"]
auteur = data ["author"]
>>>>>>> request
