numero=int(input("Escreva um número para que seja feita as divisões e multiplicações seguindo a regra, até que o número final seja 1.\n\n* Caso o número seja ímpar, multiplique por 3 e adicione 1\n* Caso o número seja par, apenas divida por 2.\n\nA seguir, digite o número: "))
print("\n")
while numero!=1:
  resultado=numero%2
  if resultado!=0:
    numero=numero*3+1
    print("{:.0f}".format(numero))
  else:
    numero=numero/2
    print("{:.0f}".format(numero))
