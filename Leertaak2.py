# - Testcode met if statements
# - Probleem 1
#print("Welkom bij Discotheek Venus, om dit pand te betreden moet u 16 jaar of ouder zijn.")
#print("Voer nu uw leeftijd in:")
#leeftijd = float(input())
#
#if (leeftijd < 16):
#    print("Sorry u bent nog te jong, onze excuses!")
#else:
#    print("U bent oud genoeg, welkom bij Venus!")

# - Probleem 2
#print("De maximumsnelheid van de Westelijke Randweg N208 is 70km/h. Voer de snelheid van de overtreder in:")
#geredensnelheid = float(input())
#
#if (geredensnelheid < 71):
#    print("De overtreder heeft niet te hard gereden. Hierop volgt geen boetebedrag")
#else:
#    if (geredensnelheid < 74):
#        print("De overtreder reed binnen de correctie marges van 3km/h, hierop volgt geen boetebedrag.")
#    else:
#        boete = (geredensnelheid - 70)*10
#        administratieboete = 25
#        print("De overtreder heeft " + str(round((geredensnelheid - 70))) + "km/h te hard gereden.")
#        print("De boete hiertegenover is: " + str(round((boete+administratieboete))) + " euro, inclusief 25 euro administratie")

# - Probleem 3
#print("Welkom bij de Bibliotheek, het lidgeld bedraagd 5 euro 26 en jonger, 10 euro daarboven.")
#print("Wat is uw leeftijd?")
#
#leeftijd = float(input())
#if (leeftijd < 27):
#    print("Het lidgeld bedraagd 5 euro voor u omdat u 26 of jonger bent, dankuwel!")
#else:
#    print("Het lidgeld bedraagd 10 euro voor u omdat u ouder dan 26 bent, dankuwel!")

# - Probleem 4
#print("Is het wezen groen, blauw, rood of geel")
#wezen = input()
#
#if (wezen.lower() == "groen"):
#    print("Het antwoord is goed, u krijgt 5 punten!")
#elif (wezen.lower() == "blauw"):
#    print("Dat is fout! U krijgt geen punten")
#elif (wezen.lower() == "rood"):
#    print("Dat is fout! U krijgt geen punten")
#elif (wezen.lower() == "geel"):
#    print("Dat is fout! U krijgt geen punten")
#else:
#    print("Dit is geen correcte keuze")

# - Probleem 5
#print("Welkom bij het pretpark, Toegang voor mensen onder 18 is 5 euro, daarboven 10 euro")
#print("Wat is uw leeftijd?")
#
#leeftijd = float(input())
#if (leeftijd < 19):
#    print("De toegang is 5 euro voor u (18-). Loopt u maar door naar de kassa")
#else:
#    print("De toegang is 10 euro voor u (18+). Loopt u maar door naar de kassa")

# - Probleem 6
#import random
#dobbel = random.randint(1,6)
#
#print("De dobbelsteen is gegooid. Het antwoord is: " + str(dobbel))
#if (dobbel == 6):
#    print("U mag nog eens gooien!")
#    dobbel2 = random.randint(1, 6)
#    print("Uw 2e dobbelsteenpoging is: " + str(dobbel2))
#else:
#    print("Uw dobbel is geen 6, hiermee eindigd uw spel!")

# - Probleem 7
#print("Bereken uw BMI hier!")
#lengte = float(input("Geef uw lengte in cm: "))
#gewicht = float(input("Geef uw gewicht in kg: "))
#geslacht = input("Wat is uw geslacht (M/V)? ")
#if (geslacht.lower() == "v"):
#    lengtevrouw = lengte - 6
#    bmilengte = lengtevrouw / 100
#elif (geslacht.lower() == "m"):
#    bmilengte = lengte / 100
#else:
#    print("Ongeldig antwoord!")
#    exit()
#bmi = gewicht / (bmilengte * bmilengte)
#print("Uw BMI is: " + str(round(bmi)))
#if (bmi < 30):
#    print("Dit BMI niveau is goed!")
#else:
#    print("Dit BMI niveau is te hoog!")

# - Probleem 8
#getal1 = float(input("Voer getal 1 in: "))
#getal2 = float(input("Voer getal 2 in: "))
#
#print("Je hebt de variabelen: " + str(round(getal1)) + " en " + str(round(getal2)))
#print("Magie!")
#
#placeholder1 = getal1
#placeholder2 = getal2
#
#getal1 = placeholder2
#getal2 = placeholder1
#print("Je hebt de variabelen: " + str(round(getal1)) + " en " + str(round(getal2)))

# - Probleem 9
getal1 = float(input("Voer getal 1 in: "))
getal2 = float(input("Voer getal 2 in: "))
getal3 = float(input("Voer getal 3 in: "))

nummers = [getal1, getal2, getal3]
print("Op volgorde zijn ze: " + str(sorted(nummers)))