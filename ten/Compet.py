class Compet:
  def __init__(self, pokrt, play1, play2):
    self.pokrt = pokrt
    self.play1 = play1
    self.play2 = play2
    print (f"{play1.getName()} vs {play2.getName()}")
    
  @classmethod
  def Probability(self,rating1, rating2):
    return 1.0 * 1.0 / (1 + 1.0 * (pow(10, 1.0 * (rating1 - rating2) / 400)))
  