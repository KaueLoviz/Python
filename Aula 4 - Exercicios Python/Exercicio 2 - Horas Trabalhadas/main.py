##############################################################################
# Exercícios Aula 4 - Slide
# Nome: Kauê Loviz de Oliveira
# Faculdade: Universidade Cruzeiro do Sul
# Data: 22/04/2022
# Site: https://github.com/KaueLoviz
##############################################################################

print("\nExercício 2 - Horas Trabalhadas\n")

nome = input("Digite seu nome: ")

print("Digite 1 - para 1º Turno")
print("_____________________________")
print("Digite 2 - para 2º Turno")
print("_____________________________")
print("Digite 3 - para 3º Turno")
print("_____________________________")

turno = int (input("Digite seu Turno: "))

hrstb = int (input("Digite sua quantidade de hora(s) trablhada(s): "))

if(turno==1):
    salariobruto = 37.50 * hrstb
    print ("Salário Bruto : R$ %.2f" %salariobruto,"\n")
    print("O funcionário ",nome, "+ o Salário Bruto é de: R$ %.2f" %salariobruto)
    print("Fim do programa")
else:
    if(turno==2):
        salariobruto = 37.50 * hrstb
        print ("Salário Bruto : R$ %.2f" %salariobruto,"\n")
        print("O funcionário ",nome, "+ o Salário Bruto é de: R$ %.2f" %salariobruto)
        print("Fim do programa")
    else:
        if(turno==3):
            salariobruto = 45.00 * hrstb
            print ("Salário Bruto : R$ %.2f" %salariobruto,"\n")
            print("O funcionário ",nome, "+ o Salário Bruto é de: R$ %.2f" %salariobruto)
            print("Fim do programa")	 
        else:
            if(turno>3):
                print("Opção invalida!")
                print("Fim do programa")