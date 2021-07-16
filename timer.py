import json


class Timer:
  
  def __init__(self, initial):
    self.StartingTime = json.load(open('game.json', 'rb'))['Clock']['StartTime']
    initial = self.StartingTime
    self.Seconds = initial
   
  def update(self):
    self.Seconds -= 1

  def is_finished(self):
    if self.Seconds == 0:
      return True
    return False
