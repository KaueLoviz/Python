def area(base, alt):
    res = base * alt / 2
    return(res)

base = int(input("Digite o valor da base do triângulo: "))
alt = int(input("Digite o valor da altura do triângulo: "))
print("A área do triângulo é: ", area(base,alt))