aluno1, aluno2, aluno3, aluno4 = str(input("A seguir, digite o nome de quatro alunos, para que sejam divididos em duplas. Além disso, cada dupla será organizada em ordem alfabética e dividida por ordem alfabética:\n\nDigite o nome do primeiro aluno: ")), str(input("Digite o nome do segundo aluno: ")), str(input("Digite o nome do terceiro aluno: ")), str(input("Digite o nome do quarto aluno: "))
lista=[aluno1,aluno2,aluno3,aluno4]
lista.sort()

if (lista[0]==lista[1]==lista[2]==lista[3]):
  print("\nNão pode formar grupo.")
elif (lista[0]==lista[1] and lista[0]==lista[2]) or (lista[1]==lista[2] and lista[1]==lista[3]):
  print("\nNão pode formar grupo.")
elif lista[0]!=lista[1] and lista[2]!=lista[3]:
  print("\nDupla 1:",lista[0],"e",lista[1], "\nDupla 2:",lista[2],"e",lista[3])
elif lista[0]!=lista[2] and lista[1]!=lista[3]:
  print("\nDupla 1:", lista[0],"e",lista[2], "\nDupla 2:", lista[1],"e",lista[3]) 
else:
  print("\nDupla 1:", lista[0],"e",lista[3], "Dupla 2:", lista[1],"e",lista[2])
