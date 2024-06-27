from bs4 import BeautifulSoup
import requests



response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
web_page= response.text



soup = BeautifulSoup(web_page, 'html.parser')

section = soup.find_all(name="h3", class_="title")
print(section)
movies = []
for movie in section:
    mov = movie.getText()
    movies.append(mov.split()[1:])
movies.reverse()

print(movies)

# Open the file in 'w' mode to write, and use 'with' to ensure proper file handling
with open("movies.txt", "w", encoding="utf-8") as file:
    # Iterate through the movies and write each one to a new line in the file
    for index, movie in enumerate(movies, start=1):
        file.write(f"{index}) {' '.join(movie)}\n")