#Aufgabe: Wörterbuch DE --> EN

woerterbuch_deutsch = ["Apfel", "Birne", "Kirsche", "Melone", "Marille", "Pfirsich"]
woerterbuch_englisch = ["apple", "pear", "cherry", "melon", "apricot", "peach"]

# 1. Ermittlung Länge Wörterbuch (= Anzahl Einträge)

max = len(woerterbuch_deutsch)

# 2. Eingabe

eingabe = input("Deutscher Begriff: ")

# 3. while-Schleife über alle Elemente

index = 0
while index < max:
    if woerterbuch_deutsch[index] ==eingabe:
        print(woerterbuch_englisch[index])
        break
    index +=1
    
if index == max:
    print("nicht gefunden")
    