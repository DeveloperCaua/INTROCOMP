numero=int(input("Digite um número inteiro qualquer, o programa irá retornar se ele é primo ou não.\n\nDigite o valor a seguir: "))

def primo_ou_nao(numero):
  n_de_divisiveis=0
  for contador in range(1, numero+1):
    if numero%contador==0:
      n_de_divisiveis=n_de_divisiveis+1
  else:
    n_de_divisiveis=n_de_divisiveis+0
    if n_de_divisiveis==2:
      print(f"\n{numero} é primo.")
    else:
      print(f"\n{numero} não é primo.")
      
primo_ou_nao(numero)
