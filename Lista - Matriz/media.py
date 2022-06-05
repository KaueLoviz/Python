nomes = []
medias = []

n = int(input("Quantos alunos deseja calcular a média? "))

for i in range(n):
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    
    nome = input("Digite o nome do aluno: ")
    
    media = (nota1 + nota2) / 2
    medias.append(media)
    nomes.append(nome)
    
    posicao = int(input("Qual aluno você deseja ver a média? "))
    
    if posicao < n:
        print("A média deste aluno é: ",medias[posicao])