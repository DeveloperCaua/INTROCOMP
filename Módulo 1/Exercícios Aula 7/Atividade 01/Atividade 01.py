lim1, lim2, num = int(input("A seguir, digite três números.\n\n* Primeiro número do intervalo;\n* Último número do intervalo;\n* Número a ser avaliado (se está ou não dentro do intervalo informado).\n\nDigite o primeiro intervalo: ")), int(input("Digite o último intervalo: ")), int(input("Digite o número a ser verificado: "))

def no_intervalo(lim1,lim2,num):
  if lim1<=num<=lim2:
    print("\nTrue")
  else:
    print("\nFalse")
no_intervalo(lim1,lim2,num)
