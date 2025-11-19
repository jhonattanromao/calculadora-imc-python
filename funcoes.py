def validaAltura(altura):
    while altura == "":
        altura = input("Digite sua altura (ex: 1.75): ")

        if altura == "":
            print("Altura não pode ser vazio.")
            continue

        try:
            altura = float(altura)
            return altura
        except:
            altura = ""
            print("Digite uma altura válida!")
            print("(Exemplo: 1.75)")
            continue

def validaPeso(peso):
    while peso == "":
        peso = input("Digite seu peso (kg): ")

        if peso == "":
            print("Peso não pode ser vazio.")
            continue

        try:
            peso = float(peso)
            return peso
        except:
            peso = ""
            print("Digite seu peso corretamente!")
            print("(Exemplo: 80)")
            continue