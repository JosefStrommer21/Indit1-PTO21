#Party Beispiel

wetter = input("Wochenendwetter - 'sonnig' oder 'regnerisch': ")

if wetter.upper() == "SONNIG":
    print("Gartenparty")
elif wetter.lower() == "regnerisch":
    print("Kellerparty")
else:
    print("Bitte entweder 'sonnig' oder 'regnerisch' eingeben!")