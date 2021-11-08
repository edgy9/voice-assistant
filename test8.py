import turtle as t
from itertools import cycle
from random import randint, random
import random


colors = ['red','orange','yellow','green','blue','purple']


ranSize = randint(40,50)
#rancol = (random(),random(),random())
color = random.choice(colors)
ranx = random.randint(-300, 350)
rany = random.randint(-300, 350)

def random_partical():
    t.penup
    t.color(color)
    #t.goto(0,0)
    t.penup
    t.goto(ranx, rany)
    t.pendown
    t.penup
    


while 2 > 1:
    random_partical()
    color = random.choice(colors)
    ranx = random.randint(-300, 350)
    rany = random.randint(-300, 350)