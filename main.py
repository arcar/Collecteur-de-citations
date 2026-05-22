import requests 


citations = []

for i in range (5):
    message = requests.get("http://api.quotable.io/random")
    data = message.json()
    citations.append({"content":data["content"],"author": data["author"]})


slides_html = ""

for quote in citations:
    content = quote['content']
    author = quote['author']

    slides_html += f"""
    <div class="slide">
        <p class="quote">“{content}”</p>
        <p class="author">— {author}</p>
    </div>
    """

html = f"""
<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<title>Carrousel de citations</title>

<style>
body {{
    margin: 0;
    height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
    background: linear-gradient(135deg, #1e3c72, #2a5298);
    font-family: Arial, sans-serif;
}}

.carousel {{
    width: 70%;
    max-width: 800px;
    overflow: hidden;
    position: relative;
}}

.slides {{
    display: flex;
    transition: transform 0.6s ease-in-out;
}}

.slide {{
    min-width: 100%;
    box-sizing: border-box;
    padding: 40px;
    color: white;
    text-align: center;
}}

.quote {{
    font-size: 2em;
    line-height: 1.4;
    margin-bottom: 20px;
}}

.author {{
    font-size: 1.2em;
    opacity: 0.8;
}}

button {{
    position: absolute;
    top: 50%;
    transform: translateY(-50%);
    background: rgba(255,255,255,0.2);
    border: none;
    color: white;
    padding: 15px;
    cursor: pointer;
    font-size: 20px;
    border-radius: 50%;
}}

.prev {{
    left: 10px;
}}

.next {{
    right: 10px;
}}
</style>
</head>

<body>

<div class="carousel">
    <div class="slides">
        {slides_html}
    </div>

    <button class="prev">&#10094;</button>
    <button class="next">&#10095;</button>
</div>

<script>
const slides = document.querySelector('.slides');
const slideElements = document.querySelectorAll('.slide');

let index = 0;

function showSlide(i) {{
    index = (i + slideElements.length) % slideElements.length;
    slides.style.transform = `translateX(${{-index * 100}}%)`;
}}

document.querySelector('.next').addEventListener('click', () => {{
    showSlide(index + 1);
}});

document.querySelector('.prev').addEventListener('click', () => {{
    showSlide(index - 1);
}});

// Rotation automatique
setInterval(() => {{
    showSlide(index + 1);
}}, 4000);
</script>

</body>
</html>
"""


# 3: Écriture du fichier HTML
fichier = "index.html"
with open(fichier, "w", encoding="utf-8") as f:
    f.write(html)
