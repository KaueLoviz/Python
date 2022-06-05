print("\nExercício 2 - Soma/Média \n")

num = soma = 0

for cont in range(0,10,1):
    num = int(input("Insira o valor: "))
    print("")
    soma = soma + num
    print("A soma é",soma)
    print("A média é",(soma/10))
    print("")

