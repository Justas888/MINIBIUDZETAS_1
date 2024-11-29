pajamos = []
islaidos = []

while True:
    print(" 1. Įveskite pajamas\n",
          "2. Įveskite išlaidas\n",
          "3. Atspausdinti pajamų eilutes\n",
          "4. Atspausdinti išlaidų eilutes\n",
          "5. Atspausdinti statistika\n",
          "q - išeiti iš programos\n",

          )
    pasirinkimas = input(">> ")
    if pasirinkimas == "q":
        break
    if pasirinkimas == "1":
        data = input("Įveskite datą (pvz., 2022-01-01): ")
        aprasymas = input("Įveskite pajamų pavadinimą (pvz., atlyginimas")
        kiekis = float(input("Įveskite sumą: "))
        pajamos.append([data, aprasymas, kiekis])

    elif pasirinkimas == "2":
        data = input("Įveskite datą (pvz., 2022-01-01): ")
        aprasymas = input("Įveskite pajamų pavadinimą (pvz., būtinosios išlaidos")
        kiekis = float(input("Įveskite sumą: "))
        islaidos.append([data, aprasymas, kiekis])

    elif pasirinkimas == "3":
        pass

print(f"Jūsų pajamos - {pajamos}")
print(f"Jūsų išlaidos - {islaidos}")
