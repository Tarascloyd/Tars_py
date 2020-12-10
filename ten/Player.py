class Player:
  def __init__(self, name, age, power, speed, skill, gskill, hskill, cskill, iskill):
    self.name = name
    self.age = age
    self.power = power
    self.speed = speed
    self.skill = skill
    self.pokrtskill=[gskill, hskill, cskill, iskill]
    self.totalw=0;
    self.totall=0;
    self.totaltitles=0;
    self.elorating=1000;
    self.maxelo=1000;

  def getName(self):
    return self.name  
  def getLevelPokrt(self, pokrt):
    return self.power + self.speed + self.skill + self.pokrtskill[pokrt]
  def getLevel(self):
    return self.power + self.speed + self.skill + sum(self.pokrtskill)/4
  def getTotalw(self):
    return self.totalw 
  def getTotall(self):
    return self.totall
  def setTotalw(self):
    self.totalw+=1 
  def setTotall(self):
    self.totall+=1
  def getTotalTitles(self):
    return self.totaltitles
  def setTotalTitles(self):
    self.totaltitles+=1
  def getEloRating(self):
    return self.elorating
  def setEloRating(self, change):
    self.elorating+=change
    if self.elorating>self.maxelo:
      self.maxelo=self.elorating
    if self.elorating<100:
      self.elorating=100