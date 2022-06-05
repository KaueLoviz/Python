def imc(peso, alt):
    res = peso / alt**2
    if (res <= 18.5):
        print("Abaixo do peso!\n")
        print("Fim do programa")
    elif (res >=18.6 and res <= 24.9):
        print("Peso ideal, Parabéns!\n")
        print("Fim do programa")
    elif (res >= 25.0 and res <= 29.9):
        print("Levemente acima do peso!\n")
        print("Fim do programa")
    elif (res >= 30.0 and res <= 34.9):
        print("Obesidade grau I!\n")
        print("Fim do programa")
    elif (res >= 35.0 and res <= 39.9):
        print("Obesidade grau II!\n")
        print("Fim do programa")
    elif (res >= 40.0):
        print("Obesidade Mórbida!\n")
        print("Fim do programa")    
    return(res)

peso = float(input("Insira o seu peso em Kg: "))
alt = float(input("Insira sua altura: "))
print("Seu IMC é: ",imc(peso,alt))