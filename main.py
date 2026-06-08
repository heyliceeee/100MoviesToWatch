from bs4 import BeautifulSoup
import requests
URL = "https://www.empireonline.com/movies/features/best-movies-2/" # set the URL
headers = { "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36", "Accept-Language": "en-US,en;q=0.9"} # set the headers

response = requests.get(URL, headers=headers) # get the response
yc_webpage = response.text # get the text

soup = BeautifulSoup(yc_webpage, "html.parser") # parse the text

span_title_movies = soup.find_all("span", class_="content_content__i0P3p") # find all the "span" tag title movies
strong_tags = [span_title_movie.find("strong") for span_title_movie in span_title_movies] # find all the "strong" tag

title_movies = [strong.get_text() for strong in strong_tags if strong is not None and ")" in strong.get_text()[:4]] # get the text of the "strong" tag
movies = title_movies[::-1] # reverse the list

with open("movies.txt", "w") as f: # open the file
    for movie in movies: # for each movie
        f.write(movie + "\n") # write the movie to the file