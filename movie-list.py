from glob import glob
from os import path
import json

from core.Movie import Movie
from core.Config import config

def get_movies ():
  files = []
  movies = []
  
  for ext in config.movie_exts:
    files.extend (glob (path.join (config.movie_path, ext)))

  for file in files:
    movies.append (Movie (file))

  return (movies)

if __name__ == '__main__':
  movies = get_movies ()

  for movie in movies:
    print ("{}: {}".format (movie.displayname, movie.year))

  if config.total:
    print ("{}\nmovies found: {}".format ('-' * 55, len(movies)))
