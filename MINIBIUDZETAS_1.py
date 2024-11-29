from datetime import datetime


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
        aprasymas = input("Įveskite pajamų pavadinimą (pvz., atlyginimas) ")
        kiekis = float(input("Įveskite sumą: "))
        pajamos.append([data, aprasymas, kiekis])

    elif pasirinkimas == "2":
        data = input("Įveskite datą (pvz., 2022-01-01): ")
        aprasymas = input("Įveskite pajamų pavadinimą (pvz., būtinosios išlaidos) ")
        kiekis = float(input("Įveskite sumą: "))
        islaidos.append([data, aprasymas, kiekis])

    elif pasirinkimas == "3":
        if pajamos:
            print("\n Pajamos: ")
            for i, income in enumerate(pajamos):
                print(f"{i+1}. Data: {income[0]}, Pavadinimas: {income[1]}, Suma: {income[2]}")
        else:
            print("Pajamų nėra.")

    elif pasirinkimas == "4":
        if islaidos:
            print("\n Išlaidos: ")
            for i, expense in enumerate(islaidos):
                print(f"{i+1}. Data: {expense[0]}, Pavadinimas: {expense[1]}, Sumas: {expense[2]}")
        else:
            print("Išlaidų nėra")

    else:
        print("Neteisingas pasirinkimas. Bandykite dar kartą")


print(f"Jūsų pajamos - {pajamos}")
print(f"Jūsų išlaidos - {islaidos}")
