import random
from ten.Player import Player
from ten.Compet import Compet

names=["Вася", "Петя", "Рома", "Костя", "Витя", "Алекс", "Стас", "Кот"]
spisok = [Player(names[x], random.randint(0,21)+17, random.randint(0,30), random.randint(0,30), random.randint(0,30), random.randint(0,60), random.randint(0,60), random.randint(0,60), random.randint(0,60)) for x in range(8)]

cmpt = Compet (2,spisok[random.randint(0,7)], spisok [random.randint(0,7)])
cmpt.match()