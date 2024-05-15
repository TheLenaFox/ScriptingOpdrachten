import math
import statistics

# - De berekening van inhoud cilinder
#print("Geef straal van de bodem van de cilinder in cm:")
#straal = float(input())
#print("Geef hoogte van de cilinder in cm:")
#hoogte = float(input())

#oppervlakte = pow(straal, 2)
#inhoud = int(oppervlakte * math.pi * hoogte)
#print(str(inhoud) + "cm3")


# - Berekening gemiddelde van 3 cijfers
#print("Geef cijfer 1")
#cijfer1 = float(input())
#print("Geef cijfer 2")
#cijfer2 = float(input())
#print("Geef cijfer 3")
#cijfer3 = float(input())

#cijfers = [cijfer1, cijfer2, cijfer3]
#gemiddelde = statistics.mean(cijfers)
#antwoord = str(round(gemiddelde, 2))

#print("Gemiddelde van de 3 (op 2 decimalen) is: " + str(antwoord))


# - Berekening celcius naar kelvin
#print("Geef temperatuur in celcius:")
#celcius = float(input())
#kelvin = celcius + 273
#print("Temperatuur in kelvin is: " + str(kelvin))


# - Berekening btw
#print("Geef bedrag in euro's:")
#bedrag = float(input())

#btw = (bedrag / 100) * 21
#print("De btw over dit bedrag (" + str(bedrag) + " EUR) is: " + str(round(btw, 2)) + " EUR")

# - Berekening inhoud kegel
#print("Geef de straal van de kegel:")
#straal = float(input())
#print("Geef de hoogte van de kegel:")
#hoogte = float(input())

#diameter = straal * straal
#inhoud = 0.33 * diameter * hoogte
#print(round(inhoud, 2))

# - Wisselkoers
print("Geef bedrag in euro's:")
euro = float(input())

dollar = euro * 1.09
print("De wisselkoers is 1.09 US Dollar per Euro. Uw bedrag is: " + str(round(euro)))
print("Het omgerekende bedrag in dollars is: " + str(dollar))