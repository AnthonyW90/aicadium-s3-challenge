from main import main
from generate_presigned_urls import create_presigned_url

urls = []
file_names = [
    "Turtle Photo by Richard Segal.jpg",
    "Turtle by Daniel Torobekov (1).jpg",
    "Turtle Photos 68744.jpg",
    "Turtle Photos by Tanguy Sauvin.jpg",
    "Turtle by Francesco Ungaro.jpg",
    "Turtle Photo Maria Bernotti.jpg",
    "Turtle by Daniel Torobekov.jpg",
]
for file in file_names:
    url = create_presigned_url("aicadium-demo", "images/" + file)
    if url is not None:
        urls.append(url)

for x in range(1000):
    main(urls[x % len(urls)])
