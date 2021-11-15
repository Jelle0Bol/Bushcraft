diesel = float(input("Hoeveel kost de dieselprijs? : "))
benzine = (244 / 12) * (diesel) * (2) + (80)
materialen = float(3.45 * 7.5) + (3 * 1.24 * 5) + (2.67 * 2) + (2 * 3.26) + (0.21 * 5) + (2.23 * 4) + (0.59 * 10)
geschikt = "Je bent wel geschikt om mee te gaan!"
helaas = "Je bent helaas niet geschikt om mee te gaan"

#print("Je moet " , (round(benzine,2))," voor benzine betalen")
#print("De materialen kosten" , (round(materialen,2)) , "euro")

print("Welkom bij BushCamp, waar ik een aantal vragen")
print("ga stellen om te kijken of jij wel geschikt hiervoor bent")
print("Ben je er klaar voor?")
print("")

sterk = int(input("Hoeveel KG kan je drukken? : "))
sterk2 = int(input("Hoeveel MM spijker kan je buigen? : "))
slim1 = int(input("Wat is je IQ? : "))
slim2 = int(input("Hoeveel seconden doe je erover om een iKEA Larsfrid buffetkast zonder handleiding in elkaar te zetten? : "))
handig1 = int(input("Hoeveel meter kan je over een sloot springen? : "))
handig2 = int(input("Hoeveel seconden doe je er over om vuurstenen en hooi in de fik te zetten? : "))
weetveel1 = int(input("Hoeveel eetbare paddenstoelen kan jij herkennen? : "))
weetveel2 = int(input("Hoeveel giftige paddenstoelen kan jij herkken? : "))
print("")

if sterk >= 100 and sterk2 >= 10:
    sterk3 = True
else:
    sterk3 = False

if slim1 >= 130 and slim2 <= 300:
    slim3 = True
else:
    slim3 = False

if handig1 >= 3 and handig2 <= 60:
    handig3 = True
else:
    handig3 = False

if weetveel1 >= 10 and weetveel2 >= 20:
    weetveel3 = True
else:
    weetveel3 = False


def sterkebeer():
    if sterk3 == True:
        print("Je bent geschikt om mee te gaan als sterke beer!")
    elif sterk3 == False:
        print("Je bent helaas niet geschikt om mee te gaan als sterke beer")

def nerd():
    if slim3 == True:
        print("Je bent geschikt om mee te gaan als nerd!")
    elif sterk3 == False:
        print("Je bent helaas niet geschikt om mee te gaan als nerd")

def harrie():
    if handig3 == True:
        print("Je bent geschikt om mee te gaan als Handige Harrie!")
    elif sterk3 == False:
        print("Je bent helaas niet geschikt om mee te gaan als Handige Harrie")

def bieb():
    if weetveel3 == True:
        print("Je bent geschikt om mee te gaan als een kennisvaardige persoon")
    elif weetveel3 == False:
        print("Je bent helaas niet geschikt om mee te gaan als een kennisvaardige persoon")

print("We zijn klaar met de test!")
print("De uitslag is : ")
sterkebeer()
print("En : ")
nerd()
print("Vervolgens : ")
harrie()
print("Ten slotte : ")
bieb()


