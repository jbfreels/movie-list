# movie-list

List the contents of the 'movies' folder on my NAS.

## setup

Nothing crazy, just basic python. Tested with _Python 3.7.4 64-bit_.

## filename

I keep all my files sorted as `MOVIE NAME (YEAR).ext` in a single folder. This project would need modifications to support a different structure.

## class Movie

- _path_: full local system path to file
- _dirname_: directory file is contained
- _filename_: filename with extension
- _displayname_: filename without extension
- _movie_: parsed out movie name
- _year_: parsed out movie year

## todo

- subtitle support
  - do subtitles exist
  - get subtitles? Not sure I'll incorporate this year as I have another project in the works to manage media.
- output format
