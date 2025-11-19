import funcoes

while True:
    altura = ""
    peso = ""

    altura = funcoes.validaAltura(altura)
    peso = funcoes.validaPeso(peso)

    confirma = input(f"Sua altura é {altura}mt e seu peso é {peso}kg? [S/N]: ").upper()

    if confirma == "S":
        resultado = peso / (altura ** 2)
        print(f"O seu IMC é: {round(resultado, 2)}")

        if resultado < 18.5:
            print("Classificação: Magreza")
        elif resultado < 24.9:
            print("Classificação: Normal")
        elif resultado < 29.9:
            print("Classificação: Sobrepeso")
        elif resultado < 39.9:
            print("Classificação: Obesidade")
        else:
            print("Classificação: Obesidade Grave")

        confirma = input(f"Deseja calcular novamente? [S/N]: ").upper()

        if confirma == "S":
            continue
        else:
            break
    else:
        print("Vamos tentar novamente...")
        continue
