print(“DIGITAL LIFE // SYSTEM START”)
egg = "Digi-Ei"
print(egg)

hatch_progress = 0

while hatch_progress < 100:
    action = input("Berühre das Digi-Ei? (ja/nein): ")

    if action == "ja":
        hatch_progress = hatch_progress + 10
        print("Schlüpf-Fortschritt:", hatch_progress, "%")
    else:
        print("Das Digi-Ei wartet...")


if hatch_progress >= 100:
    print("Das Digi-Ei schlüpft!")