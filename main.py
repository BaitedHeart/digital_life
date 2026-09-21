print("DIGITAL LIFE // SYSTEM START")

egg = "Digi-Ei"
print(egg)

hatch_progress = 0
bond = 0
warmth = 0

while hatch_progress < 100:
    action = input("Aktion wählen (berühren/wärmen/warten): ")

    if action == "berühren":
        hatch_progress = hatch_progress + 10
        bond = bond + 1
        print("Schlüpf-Fortschritt:", hatch_progress, "%")

    elif action == "wärmen":
        hatch_progress = hatch_progress + 20
        warmth = warmth + 1
        print("Schlüpf-Fortschritt:", hatch_progress, "%")

    elif action == "warten":
        print("Das Digi-Ei wartet...")

    else:
        print("Unbekannte Aktion.")

if hatch_progress >= 100:
    print("Das Digi-Ei schlüpft!")

    if bond > warmth:
        digimon = "Bondmon"
    elif warmth > bond:
        digimon = "Flaremon"
    else:
        digimon = "Balancemon"

    print("Es schlüpft:", digimon)