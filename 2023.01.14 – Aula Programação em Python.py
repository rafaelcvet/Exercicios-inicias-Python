#2023.01.14 – Aula Programação em Python Exercício 4.1
print('{:=^60}'.format("Exercício - Aula Programação em Python"))
nome = input("Digite o nome do Aluno: ")
bimestre = (int(input("Digite o número de Bimestres: ")))
nota = []
soma = 0

for nota in range(bimestre):
  nota = int(input("Digire a Nota: "))
  soma += nota
media = soma/bimestre
print("-------------------")

print("Nome:",nome)
print("Média",media)

if media >= 7:
  print("Aprovado")
elif media>= 6:
  print("Exame")
else:
  print("Reprovado")