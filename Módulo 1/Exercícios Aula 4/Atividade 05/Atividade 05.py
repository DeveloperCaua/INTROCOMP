aluno1, aluno2, aluno3, aluno4 = str(input("A seguir, digite o nome de quatro alunos, para que sejam divididos em duplas. Além disso, cada dupla será organizada em ordem alfabética:\n\nDigite o nome do primeiro aluno: ")), str(input("Digite o nome do segundo aluno: ")), str(input("Digite o nome do terceiro aluno: ")), str(input("Digite o nome do quarto aluno: "))

if (aluno1==aluno2==aluno3==aluno4):
  print("\nNão pode formar grupo.")
elif (aluno1==aluno2 and aluno1==aluno3) or (aluno2==aluno3 and aluno2==aluno4):
  print("\nNão pode formar grupo.")
elif aluno1!=aluno2 and aluno3!=aluno4:
  print("\nDupla 1:", aluno1,"e", aluno2, "\nDupla 2:",aluno3, "e", aluno4)
elif aluno1!=aluno3 and aluno2!=aluno4:
  print("\nDupla 1:", aluno1,"e", aluno3, "\nDupla 2:", aluno2, "e", aluno4) 
else:
  print("\nDupla 1:", aluno1,"e", aluno4, "Dupla 2:", aluno2, "e", aluno3)
