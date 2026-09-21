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

    hunger = 0
    energy = 100

    while True:
        action = input("Aktion wählen (füttern/spielen/schlafen/status): ")

        if action == "status":
            print("Hunger:", hunger)
            print("Energie:", energy)

        elif action == "füttern":
            hunger = max(0, hunger - 20)
            print(digimon, "wurde gefüttert.")
            print("Hunger:", hunger)

        elif action == "spielen":
            if energy >= 15:
                energy = energy - 15
                bond = bond + 1
                print(digimon, "spielt mit dir.")
                print("Energie:", energy)
                print("Bindung:", bond)
            else:
                print(digimon, "ist zu müde zum Spielen.")

        elif action == "schlafen":
            energy = min(100, energy + 30)
            print(digimon, "ruht sich aus.")
            print("Energie:", energy)

        hunger = min(100, hunger + 5)

        if hunger >= 100:
            print(digimon, "hat sehr großen Hunger!")