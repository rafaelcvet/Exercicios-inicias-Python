print('{:=^60}'.format("Exercício - Aula Programação em Python"))
nome = input("Digite o nome do Aluno: ")
bimestre = (int(input("Digite o número de Bimestres: ")))
nota = []
soma = 0

for nota in range(bimestre):
  nota = float(input("Digire a Nota: "))
  while nota>10 or nota<0:
    nota = float("Digite uma nota valida: ")
  soma += nota

media = soma/bimestre
print("-------------------")

print("Nome:",nome)
print("Média",round(media,1))

if media >= 7:
  print("Aprovado")
elif media>= 6:
  print("Exame")
else:
  print("Reprovado)")
