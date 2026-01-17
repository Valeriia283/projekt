"""
Bulls & Cows – školní projekt

autor: Valeriia283
email: valeriasandrachuk@gmail.com
"""

import random

# Úvodní text
print("Ahoj!")
print("-----------------------------------------------")
print("Vygeneroval jsem pro tebe náhodné čtyřmístné číslo.")
print("Zahrajeme si hru Bulls and Cows.")
print("-----------------------------------------------")

# Vytvoření tajného čtyřmístného čísla
cisla = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
prvni_cislice = random.choice(cisla)
cisla.remove(prvni_cislice)
cisla.append("0")

tajne_cislo = prvni_cislice
for i in range(3):
    vybrane_cislo = random.choice(cisla)
    tajne_cislo += vybrane_cislo
    cisla.remove(vybrane_cislo)

pocet_pokusu = 0

# Hlavní smyčka hry
while True:
    tip = input("Zadej číslo:\n-----------------------------------------------\n>>> ")
    pocet_pokusu += 1

    # Kontrola vstupu od uživatele
    if not tip.isdigit():
        print("Zadej pouze číslice.")
        continue

    if len(tip) != 4:
        print("Číslo musí mít přesně 4 číslice.")
        continue

    if tip[0] == "0":
        print("Číslo nesmí začínat nulou.")
        continue

    if len(set(tip)) != 4:
        print("Číslice se nesmí opakovat.")
        continue

    bulls = 0
    cows = 0

    # Vyhodnocení bulls a cows
    for i in range(4):
        if tip[i] == tajne_cislo[i]:
            bulls += 1
        elif tip[i] in tajne_cislo:
            cows += 1

    # Kontrola výhry
    if bulls == 4:
        print("-----------------------------------------------")
        print("Správně! Uhodla jsi tajné číslo.")
        print(f"Počet pokusů: {pocet_pokusu}")
        print("-----------------------------------------------")
        break

    # Správný tvar slov bull / bulls a cow / cows
    if bulls == 1:
        bull_text = "bull"
    else:
        bull_text = "bulls"

    if cows == 1:
        cow_text = "cow"
    else:
        cow_text = "cows"

    print(f"{bulls} {bull_text}, {cows} {cow_text}")
    print("-----------------------------------------------")
