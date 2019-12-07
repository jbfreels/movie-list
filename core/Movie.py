import os
import re

class Movie:
  def __init__ (self, path):
    # full system path to the file
    self.path = path

    # directory only
    self.dirname = os.path.dirname (path)

    # filename only
    self.filename = os.path.basename (path)

    # filename without extension
    self.displayname, self.ext = os.path.splitext (self.filename)

    # placeholders 
    self.movie = self.filename
    self.year = None

    # check for year in filename
    match = re.match(r".*([1-3][0-9]{3})", self.displayname)
    if match is not None:
      # found year in filename
      self.year = match.group(1)

      # name of the movie without year
      self.movie = self.filename.rsplit(' ', 1)[0]

  # check for subtitles
  # !TODO: add code to check for matching srt
  def subtitles (self):
    return False