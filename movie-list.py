from glob import glob
from os import path

from core.Movie import Movie

MOVIE_PATH = "/mnt/lilnas/movies"
MOVIE_EXTS = ("*.avi", "*.mp4", "*.m4v", "*.mkv")

def get_movies ():
  files = []
  movies = []
  
  for ext in MOVIE_EXTS:
    files.extend (glob (path.join (MOVIE_PATH, ext)))

  for file in files:
    movies.append (Movie (file))

  return (movies)

if __name__ == '__main__':
  movies = get_movies ()

  for movie in movies:
    print ("{}: {}".format (movie.displayname, movie.year))

  print ("{}\nmovies found: {}".format ('-' * 55, len(movies)))
