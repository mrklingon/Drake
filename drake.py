import time
import random
import board
import neopixel
import random
import touchio
from ncount import *
from prt import *
from wise import *

#
#based on https://github.com/DeaconDesperado/pydrake/blob/master/drake.py
#
# see https://en.wikipedia.org/wiki/Drake_equation

# set up touch for input
touch1 = touchio.TouchIn(board.TOUCH1)
touch2 = touchio.TouchIn(board.TOUCH2)



def placeNM():
    #build a random star name 
    start = ["Gi","Ro","Ah","Mi","Pa","Ki","Re","Sy","Th","Zo"]
    mid = ["eu","af","gh","uu","a","e","i","o","u","y"]
    end = ["nk","as","of","z","d","n","ll","ah","ei","ie"]

    Place = random.choice(start)+random.choice(mid)+random.choice(end)
    return (Place)

REPL = True

def drake():
	R = 1E11
	Fp = random.uniform(0.1,0.3)
	Ne = random.randrange(1,5)
	Fl = random.uniform(0.1,0.5)
	Fi = random.uniform(0.01,0.2)
	Fc = random.uniform(0.01,0.2)
	L = daysearth()
	prt (('\nHow many alien civilizations? \n'),REPL)
	prt (('Number of stars in the Milky Way '+ str(R)),REPL)
	prt (('Fraction of stars with planetary systems '+str(Fp)),REPL)
	prt (('Number of planets suitable for life '+ str(Ne)),REPL)
	prt (('Fraction of suitable planets that develop life '+  str(Fl)),REPL)
	prt (('Fraction of life that becomes sentient and eventually intelligent '+ str(Fi)),REPL)
	prt (('Fraction of intelligent life that advances to the point of communication '+ str(Fc)),REPL)
	prt (('Adjustment for incidence of self-destruction '+ str(L)),REPL)
	N = int((R*Fp*Ne*Fl*Fi*Fc*L)+.5)
	prt (("Possible number of civilizations: " + str(N)+"\n\n"),REPL)
	return N

def daysearth():
	age = 4.54E7
	indays = age*365
	cc = 50*365
	L = cc/indays
	return L

if (not REPL):
        Val = 0
        while Val == 0 :
                compthink()
                if touch1.value:
                        Val = Val +1
                if touch2.value:
                        Val = Val +2
                        
count = drake()

prt(getWD('sagan'),REPL)

while True:

    Val = 0
    if touch1.value:
        Val = Val +1
        touched = time.monotonic()
    if touch2.value:
        Val = Val +2
        touched = time.monotonic()

    if Val == 1: #calculate count
        compthink()
        count = drake()
        prt(getWD('sagan'),REPL)
        

    if Val == 2 : #display places
        blinknum(1,blue)
        prt("0: Earth",REPL)
        for i in range(count):
            prt((str(i+1)+": "+placeNM()),REPL)
    time.sleep(.25)
