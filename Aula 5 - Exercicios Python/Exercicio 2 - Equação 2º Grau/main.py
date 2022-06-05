##############################################################################
# Exercícios Aula 5 - Slide
# Nome: Kauê Loviz de Oliveira
# Faculdade: Universidade Cruzeiro do Sul
# Data: 26/04/2022
# Site: https://github.com/KaueLoviz
##############################################################################

print("\nExercício 2 - Equação 2° Grau\n")

a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))
c = int(input("Digite o valor de c: "))

if(a != 0):
    delta = (b ** 2) - (4*a*c)
    print("Delta: %.2f" % delta)
    
    if(delta < 0):
        print("\nNão é Equação do 2° Grau, pois delta = 0!\n")
        print("Fim do programa")
    else:
        x1 = (-b + delta**0.5)/(2*a)
        print("X1 = %.2f" % (x1))
        
        if(delta > 0):
            x2 = (-b - delta**0.5)/(2*a)
            print("X1 = %.2f" % (x2))
        else:
            print("\nAmbas raízes iguais!\n")
            print("Fim do programa")
else:
    print("\nNão possui raízes reais!(a = 0)\n")
    print("Fim do programa")