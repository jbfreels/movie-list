import yaml
import json

class Config:
  movie_path = ""
  movie_exts = ""
  total = False
  sort = {}

  def __init__ (self, path="config.yml"):
    with open ("config.yml", 'r') as yml:
      self.yaml = yaml.load (yml, Loader=yaml.Loader)
      self.__dict__.update (self.yaml)

  def __str__ (self):
    return json.dumps(self.yaml)

config = Config ()