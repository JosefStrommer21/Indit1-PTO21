# if [Bedingung 1] :
#      Anweisung 1
# elif [Bedingung 2]
#      Anweisung 2
# elif [Bedingung 3]
#      Anweisung 3
# else:
#      Anweisung 4 (default Anweisung)

strZahl1 = input("Eingabe 1. Zahl: ")
floatZahl1 = float(strZahl1)
strZahl2 = input("Eingabe 2. Zahl: ")
floatZahl2 = float(strZahl2)

# die kleinere Zahl soll von der größeren Zahl subtrahiert werden

if floatZahl1 > floatZahl2:
    floatDifferenz = floatZahl1 - floatZahl2
    floatNegDifferenz = floatZahl2 - floatZahl1
    print("Differenz: ", floatDifferenz)
    print("Differenz: ", floatNegDifferenz)
elif floatZahl2 > floatZahl1:
    floatDifferenz = floatZahl2 - floatZahl1
    floatNegDifferenz = floatZahl1 - floatZahl2
    print("Differenz: ", floatDifferenz)
    print("Differenz: ", floatNegDifferenz)
else:
    print("Differenz wäre 0")

    