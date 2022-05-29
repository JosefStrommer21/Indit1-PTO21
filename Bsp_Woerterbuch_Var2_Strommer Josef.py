# Ändern Sie das Wörterbuch-Beispiel aus Lab 2 wie folgt:
#
# 1) Verwendung eines od. mehrerer Assoziativ-Arrays (Dictionary)
# 2) Funktion, um übersetzte Begriffe auszulesen
# 3) Funktion, um dem Wörterbuch neue Begriffe hinzuzufügen

wb = {"dog":"HUnd", "apple":"Apfel", "cat":"Katze", "red":"rot", "hello":"hallo", "peach":"Pfirsich"}

print("Welcome to en2ger, please select the desired function")
print("Choose [T] to translate")
print("Choose [A] to add new word")
    

    
correct = False
    
while correct == False:       
    eing = input("Enter a function: ")    
    
    if eing == "T":
       
       
        word=input("Please enter your word: ") #Auslesen
        if word in wb:
            print("translation: ",wb[word]) #Übersetzung
        else:
            print('not found')
    elif eing == "A":
        #correct = True #korrekte Eingabe
        wb[input('English word:')] = input('German translation:') 
        
        
        
    else:
        print("Unknown answer")
