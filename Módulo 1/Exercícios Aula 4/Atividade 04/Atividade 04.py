A, lista, chute = int(input("Escreva um número A inteiro aleatório para ser adivinhado: ")), [], int(input("\nAgora, comece a digitar números inteiros até acertar o valor de A:\n\n"))

lista.append(chute)
if chute>A:
  print("\nChute alto\n")
elif chute<A:
  print("\nChute baixo\n")
elif chute==A:
  print("\nAcertou!\n")
  print(lista)
while chute!=A:
  chute=int(input())
  lista.append(chute)
  if chute>A:
    print("\nChute alto\n")
  elif chute<A:
    print("\nChute baixo\n")
  elif chute==A:
    print("\nAcertou!\n")
    print("Aqui estão todas as suas tentativas:", lista)
