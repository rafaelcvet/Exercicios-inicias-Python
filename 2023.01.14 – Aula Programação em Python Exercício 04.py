print('{:=^60}'.format("Exercício - Aula Programação em Python"))
nome = input("Digite o nome do Aluno: ")
nota1 = int(input("Digite nota primeiro bimestre: "))
nota2 = int(input("Digite nota segundo bimestre: "))
nota3 = int(input("Digite nota terceiro bimestre: "))
nota4 = int(input("Digite nota quarto bimestre: "))

notas = (nota1,nota2,nota3,nota4)

media = (nota1 + nota2 + nota3 + nota4)/4
print("Nome:",nome)
print("Média",media)

if media >= 7:
  print("Aprovado")
elif media>= 6:
  print("Exame")
else:
  print("Reprovado)")