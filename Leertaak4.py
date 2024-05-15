import math
import random
import statistics
#fruitlist = ["appel", "banaan", "kers", "druif", "aardbei"]
#fruitlist[2] = "pruim"
#print(fruitlist[2])
#fruitlist = ["appel", "banaan", "kers", "druif", "aardbei"]
#fruitlist.sort()
#print (fruitlist)
#fruitlist = ["appel", "banaan", "kers", "druif", "aardbei"]
#fruitlist.insert(3,"peer")
#print (fruitlist)
#fruitlist = ["appel", "banaan", "kers", "druif", "aardbei"]
#del fruitlist[2]
#print (fruitlist)
#fruitlist = ["appel", "banaan", "kers", "druif", "aardbei"]
#fruitlist.pop()
#print (fruitlist)
#fruitlist = ["appel", "banaan", "kers", "druif", "aardbei"]
#fruitlist.remove("banaan")
#print (fruitlist)
#fruitlist = ["appel", "banaan", "kers", "druif", "aardbei"]
#print (len(fruitlist))


# - Probleem 1
#kleuren = ["blauw", "geel", "groen"]
#print("De trui is " + kleuren[2])

# - Probleem 2
#hobbies = ["gamen", "voetballen", "zingen"]
#print("Zullen we gaan " + hobbies[0] + " morgen?")

# - Probleem 3
#games = ["Cities Skylines 2", "Terraria", "Minecraft", "Satisfactory", "Euro Truck Simulator 2", "Transport Fever 2"]
#for element in games:
#    print(element)
#print(games [0:3])

# - Probleem 4
#plaatsen = ["Norway", "Denmark", "United States", "Canada", "Luxembourg", "Germany", "Japan"]
#for element in plaatsen:
#    print(element)
#print("")
#invoer = input("Alfabetisch of Reversed? ")
#if (invoer.lower() == "abc"):
#    plaatsen.sort()
#    for element in plaatsen:
#        print(element)
#elif (invoer.lower() == "cba"):
#    plaatsen.sort(reverse=True)
#    for element in plaatsen:
#        print(element)
#print("")
#plaatsen.append("England")
#del plaatsen[2]
#for element in plaatsen:
#    print(element)

# - Probleem 5
#cijfers = [10, 20, 30, 40, 50, 60, 70, 80]
#antwoord = cijfers[1]+cijfers[3]
#print("Het antwoord van cijfer 2 + cijfer 4 is:", antwoord)
#gemiddelde = statistics.mean(cijfers)
#print("Het gemiddelde is:", gemiddelde)
#print("Het hoogste cijfer is:", max(cijfers))
#print("Het laagste cijfer is:", min(cijfers))

# - Probleem 6
#print(random.randint(30,345))

# - Probleem 7
#dobbel = random.randint(1,6)
#print("De dobbelsteen is gegooid. Het antwoord is: " + str(dobbel))

# - Probleem 8
#kaartKleur = ["Harten", "Schoppen", "Klaveren", "Ruiten"]
#kaartWaarde = ["Boer", "Vrouw", "Heer", "Aas", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
#
#print("Alle kleuren van de kaarten:")
#for element in kaartKleur:
#    print(element)
#print("")
#print("Alle waardes van de kaarten:")
#for element in kaartWaarde:
#    print(element)
#print("")
#
#print("Een willekeurige kleur voor een kaart is:", random.choice(kaartKleur))
#print("Een willekeurige waarde voor een kaart is:", random.choice(kaartWaarde))
#print("Speelkaart:", random.choice(kaartWaarde), random.choice(kaartKleur))

# - Probleem 9
snelwegen = ["A1", "A4", "A5", "A7", "A10"]
provinciewegen = ["N200", "N201", "N205", "N208", "N232"]

print("Lijst met belangrijkste snelwegen die ik heb gereden:")
for element in snelwegen:
    print(element)
print("")
print("Bare list met provinciewegen:", provinciewegen)

provinciewegen.append("N206")
print("Nu inclusief de Vogelenzangseweg:", provinciewegen)
provinciewegen.sort()
print("Weer gesorteerd:", provinciewegen)

snelwegen.insert(0, "A27")
print("Snelwegen gecorrigeerd met Rijksweg 27:", snelwegen)
del snelwegen[5]
print("Zonder de vervelende ringweg:", snelwegen)

langsteweg = snelwegen.pop(4)
snelwegen.append("A10")
print("De langste snelweg van NL is de", langsteweg)
print("De overige wegen zijn:", snelwegen)

print("In totaal heb ik " + str(len(snelwegen)) + " belangrijke snelwegen afgereden in Nederland (Exclusief de anderen die ik heb afgereden)")
print("Een willekeurige snelweg:", random.choice(snelwegen))
exit()