numero=int(input("Digite um número inteiro x qualquer, o programa irá retornar o seu fatorial (!x)\n\nDigite o número a seguir: "))

def fatoração(numero):
  r=1
  for contador in range(1, numero+1):
    r=r*contador
  print("\nO fatorial de {} é {}.".format(numero,r))
fatoração(numero)
