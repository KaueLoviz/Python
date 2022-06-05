##############################################################################
# Exercícios Aula 3 - Slide
# Nome: Kauê Loviz de Oliveira
# Faculdade: Universidade Cruzeiro do Sul
# Data: 19/04/2022
# Site: https://github.com/KaueLoviz
##############################################################################
from math import radians, sin, cos, tan
print("")
print("Exercício 5 - Ângulos \n")

angulo = float(input("Digite o ângulo que você deseja: "))
print("")

seno = sin(radians(angulo))
print("O angulo de {} tem o Seno de {:.2f}".format(angulo, seno))
print("")

cosseno = cos(radians(angulo))
print("O angulo de {} tem o Cosseno de {:.2f}".format(angulo, cosseno))
print("")

tangente = tan(radians(angulo))
print("O angulo de {} tem a Tangente de {:.2f}".format(angulo, tangente))
print("")
print("Fim do programa")