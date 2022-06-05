##############################################################################
# Exercícios Aula 4 - Slide
# Nome: Kauê Loviz de Oliveira
# Faculdade: Universidade Cruzeiro do Sul
# Data: 26/04/2022
# Site: https://github.com/KaueLoviz
##############################################################################

print("\nExercício 4 - Conta Fixa\n")

agua = float(input("Digite o valor da sua conta de Água: "))
luz = float(input("\nDigite o valor da sua conta de Luz: "))
telefone = float(input("\nDigite o valor da sua conta de Telefone: "))
salario = float(input("\nDigite o valor do seu Salário: R$"))

contas = agua + luz + telefone

if(salario > contas):
    salarioResto = salario - contas
    print("O valor restante do salário após pagar as contas é de: R$",format(salarioResto,".2f"))
    print("Fim do programa")
else:
    if(salario < contas):
        print("Salário Insuficiente para pagar as contas!")
        print("Fim do programa")