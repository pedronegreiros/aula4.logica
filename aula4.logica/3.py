while True:
    nome = str(input("digite um nome: "))

    if len(nome) > 3:
        break
    else:
        print("invalido")

while True:
    idade = int(input("digite uma idade: "))

    if idade >= 0 and idade <= 150:
        break
    else:
        print("invalido")

while True:
    salario = float(input("digite seu salario: "))

    if salario > 0:
        break
    else:
        print("invalido")

while True:
    sexo = str(input("qual seu sexo? ")).upper()

    if sexo == "M" or sexo == "f":
        break
    else:
        print("invalido")

while True:
    estado = str(input("digite seu estado civil: ")).upper()

    if estado == "s" or estado == "c" or estado == "v" or estado == "d":
        break
    else:
        print("invalido")




    

    