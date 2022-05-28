#!/usr/bin/env python3
from glob import glob
from os import path

from core.Config import config
from core.Movie import Movie


def get_movies():
    files = []
    movies = []

    if config.movie_path.startswith("~"):
        config.movie_path = path.expanduser(config.movie_path)

    for ext in config.movie_exts:
        files.extend(glob(path.join(config.movie_path, ext)))

    for file in files:
        movies.append(Movie(file))

    return movies


if __name__ == "__main__":
    movies = get_movies()

    if config.sort["enabled"]:
        movies.sort(key=lambda x: x.displayname, reverse=config.sort["reverse"])

    for movie in movies:
        print("{}: {}".format(movie.displayname, movie.year))

    if config.total:
        print("{}\nmovies found: {}".format("-" * 55, len(movies)))
