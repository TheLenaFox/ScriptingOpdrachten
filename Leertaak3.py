# - Probleem 1
# print("Hoeveel dagen is uw boek te laat ingeleverd?")
# datum = float(input("Dagen: "))
#
# if (datum < 1):
#    print("Uw boek is niet te laat ingeleverd, hierop volgt geen boete!")
# elif (datum < 6):
#    boete = 0.25 * datum
#    print("Uw boek is minder dan 6 dagen te laat, uw boete is: " + str(boete) + " euro")
# elif (datum < 11):
#    boete = 0.50 * datum
#    print("Uw boek is minder dan 11 dagen te laat, uw boete is: " + str(boete) + " euro")
# elif (datum > 10):
#    boete = 1 * datum
#    print("Uw boek is meer dan 10 dagen te laat, uw boete is: " + str(boete) + " euro")
# else:
#    exit()

# - Probleem 2
# print("Wat is de stand van het verkeerslicht (Rood/Groen/Geel)?")
# verkeerslicht = input()
#
# if (verkeerslicht.lower() == "groen"):
#    print("Het licht is groen, het word geel!")
# elif (verkeerslicht.lower() == "geel"):
#    print("Het licht is geel, het word rood!")
# elif (verkeerslicht.lower() == "rood"):
#    print("Het licht is rood, het word groen!")
# else:
#    print("Ongeldige toestand, probeer opnieuw!")
#    exit()

# - Probleem 3
# prijs = 0.50
# korting10 = 0.10
# korting20 = 0.20
# print("De prijs van 1 liedje is: " + str(prijs) + " euro. Uw korting kan oplopen tot " + str(korting20) + " euro.")
# aantal = float(input("Hoeveel liedjes wilt u kopen? "))

# if (aantal < 1):
#    print("Selecteer een geldig aantal!")
#    exit()
# elif (aantal < 11):
#    subtotaal = prijs * aantal
#    print("U hebt " + str(round(aantal)) + " stuks besteld, uw totaalbedrag is " + str(subtotaal) +  " euro")
# elif (aantal < 26):
#    subtotaal = (prijs - korting10) * aantal
#    kortingtotaal = korting10 * aantal
#    print("U hebt " + str(round(aantal)) + " stuks besteld, u krijgt " + str(kortingtotaal) + " euro korting, uw totaalbedrag is " + str(subtotaal) + " euro.")
# elif (aantal > 25):
#    subtotaal = (prijs - korting20) * aantal
#    kortingtotaal = korting20 * aantal
#    print("U hebt " + str(round(aantal)) + " stuks besteld, u krijgt " + str(kortingtotaal) + " euro korting, uw totaalbedrag is " + str(subtotaal) + " euro.")

# - Probleem 4
# print("Welkom bij de sponsorloop!")
# rondjes = float(input("Hoeveel rondjes heeft Piet gelopen? "))
# prijsrondje = 0.75
#
# if (rondjes < 1):
#    print("Ongeldig aantal rondjes")
#    exit()
# elif(rondjes < 15):
#    subtotaal = prijsrondje * rondjes
#    print("Piet heeft " + str(rondjes) + " rondjes gelopen. Hiervoor krijgt hij: " + str(subtotaal) + " euro")
# elif(rondjes < 25):
#    prijs = prijsrondje * 14
#    prijs15 = (prijsrondje + 0.25) * (rondjes - 14)
#    subtotaal = prijs + prijs15
#    print("Piet heeft " + str(rondjes) + " rondjes gelopen. Hiervoor krijgt hij: " + str(subtotaal) + " euro")
# elif(rondjes > 24):
#    prijs = prijsrondje * 14
#    prijs15 = (prijsrondje + 0.25) * 11
#    prijs25 = (prijsrondje + 0.75) * (rondjes - 25)
#    subtotaal = prijs + prijs15 + prijs25
#    print("Piet heeft " + str(rondjes) + " rondjes gelopen. Hiervoor krijgt hij: " + str(subtotaal) + " euro")

# - Probleem 5
print("Indentificeer uw verkeersbord hier! Wat is de vorm? (Rond/Driehoek/Vierkant)")
vorm = input()
print("En wat is de kleur? (Blauw/Wit)")
kleur = input()

if vorm.lower() == "rond" and kleur.lower() == "blauw":
    print("Het verkeersbord is een Gebodsbord")
elif vorm.lower() == "rond" and kleur.lower() == "wit":
    print("Het verkeersbord is een Verbodsbord")
elif vorm.lower() == "driehoek" and kleur.lower() == "wit":
    print("Het verkeersbord is een Waarschuwingsbord")
elif vosrm.lower() == "driehoek":
    print("Geen geldig verkeerbord")
elif vorm.lower() == "vierkant" and kleur.lower() == "blauw":
    print("Het verkeersbord is een Aanduidingsbord")
elif vorm.lower() == "vierkant":
    print("Geen geldig verkeersbord")
