from constants import *

class Photo:
  def __init__(self, id='-', year='-', description='-', place='-', url="-"):
    self.id = id
    self.year = year
    self.description = description.replace('/', '|')
    self.place = place
    self.url = url

  def __str__(self):
    return "Photo(" + self.title() + ")"

  def title(self):
    return self.year + TITLE_SEPARATOR + self.description + TITLE_SEPARATOR + self.id + TITLE_SEPARATOR + self.place
