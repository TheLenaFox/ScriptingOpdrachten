from pybricks.hubs import InventorHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = InventorHub()
# Steering = Port A
# Engine = Port B
# Platform Turntable = Port F
# Platform Up-Down - Port D
# Lamp front = Port C

stuur = Motor(Port.A)
engine = Motor(Port.B)
platformY = Motor(Port.D)
platformX = Motor(Port.F)
lamp = ColorSensor(Port.C)

platformActie = []
platformNodig = []
motorActieSnelheid = []
motorActieTijd = []
stuurActie = []
stuurRichting = []

def robotReset():
    if stuur.angle() <= -25:
        stuur.run_target(900,-60,Stop.COAST)
        stuur.run_target(900,10,Stop.COAST)
    elif stuur.angle() >= 25:
        stuur.run_target(900,60,Stop.COAST)
        stuur.run_target(900,-25,Stop.COAST)
    platformY.run(-100)
    wait(5000)
    if platformX.angle() < 350:
        platformX.run(-500)
        wait(1000)
        platformX.run_angle(-100,-310,Stop.COAST)
    elif platformX.angle() > 380:
        platformX.run(500)
        wait(1000)
        platformX.run_angle(100,-310,Stop.COAST)

actieWhile = 0
while actieWhile == 0:
    prompt = input("Nieuwe actie toevoegen? (Ja/Nee): ")
    if prompt.lower() == "ja":
        onderdeel = input("Welk onderdeel wil je aansturen? (Motor/Platform): ")
        if onderdeel.lower() == "motor":
            tijd = int(input("Hoelang moet hij bewegen? Seconde: ")) * 1000
            snelheid_raw = int(input("Welke stand snelheid? [1-10]: "))
            if snelheid_raw < 1:
                print("Geen geldige snelheid (TE LAAG)")
                break
            elif snelheid_raw > 10:
                print("Geen geldige snelheid (TE HOOG)")
                break
            else:
                snelheid = snelheid_raw * 100
            actie = input("Welke rijrichting? (Voor/Achter/Links/Rechts): ")
            if actie.lower() == "voor":
                motorActieSnelheid.append(-snelheid)
                motorActieTijd.append(tijd)
                stuurActie.append(False)
                platformNodig.append(False)
                print("Actie toegevoegd! (VOOR)")
            elif actie.lower() == "achter":
                motorActieSnelheid.append(snelheid)
                motorActieTijd.append(tijd)
                stuurActie.append(False)
                platformNodig.append(False)
                print("Actie toegevoegd! (ACHTER)")
            elif actie.lower() == "links":
                motorActieSnelheid.append(-snelheid)
                motorActieTijd.append(tijd)
                stuurActie.append(True)
                platformNodig.append(False)
                stuurRichting.append("links")
                print("Actie toegevoegd! (LINKS)")
            elif actie.lower() == "rechts":
                motorActieSnelheid.append(-snelheid)
                motorActieTijd.append(tijd)
                stuurActie.append(True)
                platformNodig.append(False)
                stuurRichting.append("rechts")
                print("Actie toegevoegd! (RECHTS)")
            elif actie.lower() == "lingo":
                hub.speaker.beep(frequency=500,duration=100)
                wait(50)
                hub.speaker.beep(frequency=900,duration=100)
                wait(50)
                hub.speaker.beep(frequency=200,duration=100)
                wait(50)
                hub.speaker.beep(frequency=300,duration=100)
                wait(50)
                hub.speaker.beep(frequency=200,duration=100)
                wait(50)
                hub.speaker.beep(frequency=200,duration=100)
                wait(50)
                hub.speaker.beep(frequency=200,duration=100)
                wait(50)
                hub.speaker.beep(frequency=200,duration=100)
                wait(50)
                hub.speaker.beep(frequency=200,duration=100)
                wait(50)
        elif onderdeel.lower() == "platform":
            print(" \n################################################")
            print("Let op! De platform vragen zijn case-sensitive!!")
            print("################################################\n ")
            platPart = input("Wil je de platform of de arm besturen? (Draaien/Arm): ")
            if platPart == "Draaien":
                actie = input("Welke kant moet hij op bewegen? (Links/Rechts/Voor): ")
                if actie == "Voor":
                    platformNodig.append(True)
                    platformActie.append("voor")
                    print("Actie toegevoegd! (VOOR)")
                elif actie == "Links":
                    platformNodig.append(True)
                    platformActie.append("links")
                    print("Actie toegevoegd! (LINKS)")
                elif actie == "Rechts":
                    platformNodig.append(True)
                    platformActie.append("rechts")
                    print("Actie toegevoegd! (RECHTS)")
            elif platPart == "Arm":
                actie = input("Wil je de arm open of dichtdoen? (Close/Open): ")
                if actie == "Close":
                    platformNodig.append(True)
                    platformActie.append("close")
                    print("Actie toegevoegd! (CLOSE)")
                elif actie == "Open":
                    platformNodig.append(True)
                    platformActie.append("open")
                    print("Actie toegevoegd! (OPEN)")
        else:
            print("Verkeerd antwoord! Typ 'Platform' of 'Motor'")
    elif prompt.lower() == "nee":
        actieWhile = 1
    else:
        print("Verkeerd antwoord, typ 'Ja' of 'Nee'")


def motorScript():
    spd = motorActieSnelheid.pop(0)
    tme = motorActieTijd.pop(0)
    stuurNodig = stuurActie.pop(0)
    if stuurNodig == True:
        stuurDir = stuurRichting.pop(0)
        if stuurDir == "links":
            stuur.run_target(900,60,Stop.COAST)
            wait(100)
            engine.run_time(spd,tme)
            wait(100)
        elif stuurDir == "rechts":
            stuur.run_target(900,-60,Stop.COAST)
            wait(100)
            engine.run_time(spd,tme)
            wait(100)
    elif stuurNodig == False:
        if stuur.angle() <= -25:
            stuur.run_target(900,-60,Stop.COAST)
            stuur.run_target(900,10,Stop.COAST)
            wait(10)
            engine.run_time(spd,tme)
        elif stuur.angle() >= 25:
            stuur.run_target(900,60,Stop.COAST)
            stuur.run_target(900,-25,Stop.COAST)
            wait(10)
            engine.run_time(spd,tme)
        else:
            engine.run_time(spd,tme)

def platformScript():
    platActie = platformActie.pop(0)
    if platActie == "close":
        platformY.run(-100)
        wait(5000)
        hub.speaker.beep(frequency=500,duration=100)
        wait(10)
        hub.speaker.beep(frequency=500,duration=100)
    elif platActie == "open":
        platformY.run(100)
        wait(5000)
        hub.speaker.beep(frequency=500,duration=100)
        wait(10)
        hub.speaker.beep(frequency=500,duration=100)
    elif platActie == "links":
        platformX.run(-500)
        wait(2000)
    elif platActie == "rechts":
        platformX.run(500)
        wait(2000)
    elif platActie == "voor":
        if platformX.angle() < 360:
            platformX.run(-500)
            wait(1000)
            platformX.run_angle(-100,-310,Stop.COAST)
        elif platformX.angle() > 370:
            platformX.run(500)
            wait(1000)
            platformX.run_angle(100,-310,Stop.COAST)

while platformNodig:
    platformNodigPrompt = platformNodig.pop(0)
    if platformNodigPrompt == False:
        motorScript()
    else:
        platformScript()

robotReset()