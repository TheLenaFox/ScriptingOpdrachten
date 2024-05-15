import math
import random


getal = 1
while int(getal) > 0:
    invoer = int(input("Geef getal: "))
    if invoer > getal:
        getal = invoer
        print("Het nieuwe hoogste getal is: " + str(getal))
    elif invoer < 1:
        getal = invoer
    else:
        print("Het hoogste getal blijft " + str(getal))
print("Getal lager gelijk aan of lager dan 0, einde script.")

"""
proefwerkcijfer = int(input("Geef cijfer: "))
teller = 0
som = 0 + proefwerkcijfer
while proefwerkcijfer <= 10 and proefwerkcijfer > 1:
    proefwerkcijfer = int(input("Geef proefwerk cijfer: "))
    som = som + proefwerkcijfer
    teller = teller + 1
gemiddelde = som / teller
print(gemiddelde)
"""
"""
getal = 0
print(getal)
while getal < 10:
    getal = getal + 2
    print(getal)
print("Klaar!")
"""
"""
goedantwoord = random.randint(0, 1000)
#print(goedantwoord)
antwoord = 0
while antwoord != goedantwoord:
    antwoord = int(input("Raad het getal! "))
    if antwoord < goedantwoord:
        print("Je moet hoger gokken!")
    elif antwoord > goedantwoord:
        print("Je moet lager gokken!")
print("Je hebt goed gegokt, het antwoord is " + str(goedantwoord))
"""
"""
spel_afgelopen = False
while spel_afgelopen == False:
    getal1 = random.randint(0,100)
    getal2 = random.randint(0,100)
    goedantwoord = getal1 + getal2
    print("De som is: " + str(getal1) + "+" + str(getal2))
    antwoord = int(input("Wat is het goede antwoord? "))
    if antwoord == goedantwoord:
        print("Goed zo, dat is correct!")
    elif antwoord != goedantwoord:
        print("Incorrect, je bent af!")
        spel_afgelopen = True
print("Bedankt voor het spelen!")
print("Het correcte antwoord was: " + str(goedantwoord))

j = -5
print(j)
while True:
    if j < 0:
        j = j + 1
        print(j)
    else:
        break

Het verschil tussen een while en do-while loop, makkelijkst om uit te leggen is dat een while loop checkt eerst voor een conditie, en als dat true is
voert hij de while loop uit. Terwijl bij een do-while loop, voert hij de while loop uit en checkt hij daarna de conditie, en als die false is stopt hij.
"""
