##############################################################################
# Exercícios Aula 5 - Slide
# Nome: Kauê Loviz de Oliveira
# Faculdade: Universidade Cruzeiro do Sul
# Data: 26/04/2022
# Site: https://github.com/KaueLoviz
##############################################################################

print("\nExercício 4 - Calculadora\n")

calcular = input("""Por favor, digite a operação matemática que gostaria de completar:
+ = Adição
- = Subtracção
* = Multiplicação
/ = Divisão: """)

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

if calcular == "+":
    print("A soma entre {} + {} = ".format(n1, n2),n1 + n2)
    print("Fim do programa")

elif calcular == "-":
    print("A subtração entre {} - {} = ".format(n1, n2),n1 - n2)
    print("Fim do programa")

elif calcular == "*":
    print("A multiplicação entre {} * {} = ".format(n1, n2),n1 * n2)
    print("Fim do programa")

elif calcular == "/":
    print("A divisão entre {} / {} = ".format(n1, n2),n1 / n2)
    print("Fim do programa")

else:
    print("Opção Inválida!")
    print("Fim do programa")
            