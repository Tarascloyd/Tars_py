import random

class Compet:
  def __init__(self, pokrt, play1, play2):
    self.pokrt = pokrt
    self.play1 = play1
    self.play2 = play2
    self.p1=0
    self.p2=0
    print (f"{play1.getName()} vs {play2.getName()}")
    
  def match(self):
    lvl1=self.play1.getLevelPokrt(self.pokrt)
    lvl2=self.play2.getLevelPokrt(self.pokrt)
    score="("
    if lvl1>lvl2:
      ver=100-round((0.5-(lvl1-lvl2)*0.005-(lvl1-lvl2)*0.00875)*100)
    else:
      ver=round((0.5-(lvl2-lvl1)*0.005-(lvl2-lvl1)*0.00875)*100)
    if ver<1: ver=1
    if ver>99: ver=99
    while self.p1<2 and self.p2<2:
      score = score + self.set(ver)
    print (str(self.p1) + " - " + str(self.p2) + score[:-2] + ")")


  
  def set(self,ver):
    g1=0
    g2=0
    verg=0
    while (g1<6 and g2<6) or (g1-g2==1 or g1-g2==-1 or g1-g2==0) and (g1!=7 and g2!=7):
      if (g1+g2)%2==0:
        verg=ver+20
      else: 
        verg=ver-20
      if verg<1: verg=1
      if verg>99: verg=99
      kubik=random.randint(0,99)
      if kubik<verg:
        g1+=1;
      else:
        g2+=1
    
    if g1>g2:
      self.p1+=1 
    else: 
      self.p2+=1
    return str(g1) + " - " + str(g2) + ", "
 
  @staticmethod
  def Probability(rating1, rating2):
    return 1.0 * 1.0 / (1 + 1.0 * (pow(10, 1.0 * (rating1 - rating2) / 400)))