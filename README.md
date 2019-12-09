# movie-list
List the contents of the 'movies' folder on my NAS.  

# setup
Nothing crazy, just basic python.  Tested with *Python 3.7.4 64-bit*.

# filename
I keep all my files sorted as `MOVIE NAME (YEAR).ext` in a single folder.  This project would need modifications to support a different structure.

# class Movie
* *path*: full local system path to file
* *dirname*: directory file is contained
* *filename*: filename with extension
* *displayname*: filename without extension
* *movie*: parsed out movie name
* *year*: parsed out movie year

# todo
* subtitle support 
  * do subtitles exist
  * get subtitles?  Not sure I'll incorporate this year as I have another project in the works to manage media.
* output format
