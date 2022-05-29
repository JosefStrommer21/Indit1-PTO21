# Schreiben Sie ein Programm, das auf 2 möglichen Versionen,
# die in der Liste aufgeführeten Personen begrüßt.
# z.B.: "Hallo Pater!"
#
# Version1: for-Schleife in Hauptprogramm, Ausgabe der Begrüßung in einem Unterprogramm
#
# Version2: for-Schleife und Ausgabe der Begrüßung in einem Unterprogramm

namen = ["Peter", "Dora", "Kevin", "Fritz", "Sarah"]

def begruessung(name):
    print("Hallo ", name)
    print("Schön dich zu sehen!")
    print("Viel Spaß mit dem Programm!")
    
def begruessung2(namensliste):
    for ein_name in namensliste:
        print("Hallo ", ein_name)
        print("Schön dich zu sehen!")
        print("Viel Spaß mit dem Programm!")
    
print("Version 1")
for name in namen:
    begruessung(name)
    
print("Version 2")
begruessung2(namen)
    
