numero =123
centena =int(numero/100)
dezena = int((numero-(centena*100))/10)
unidade = int(numero-(centena*100)-(dezena*10))


print("O número tem,",int(numero/100),"centena(s)")
print("o número tem,",dezena,"dezena(s)")
print("O número tem,",unidade,"unidade(s)")

print("seu inverso é: ",unidade,dezena,centena)