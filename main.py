import random
from ten.Player import Player
from ten.Compet import Compet

names=["Вася", "Петя", "Рома", "Костя", "Витя", "Алекс", "Стас", "Кот"]
spisok = [Player(names[x], random.randint(0,21)+17, random.randint(0,30), random.randint(0,30), random.randint(0,30), random.randint(0,60), random.randint(0,60), random.randint(0,60), random.randint(0,60)) for x in range(8)]

cmpt = Compet (2,spisok[1], spisok [3])
print (cmpt.Probability(spisok[1].getEloRating(),spisok[3].getEloRating()))