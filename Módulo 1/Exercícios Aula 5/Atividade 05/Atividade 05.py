N, adicao = int(input("A seguir, escolha um número inteiro qualquer. O programa irá retornar se ele é ou não um número perfeito.\n\n* Em matemática, um número perfeito é um número natural para o qual a soma de todos os seus divisores naturais próprios é igual ao próprio número.\n\nDigite o número a seguir: ")), 0

for divisao in range(1,N):
    if N%divisao==0:
      adicao+=divisao
    
if N==adicao:
  print(f"\n{N} é perfeito.")
    
else:
  print(f"\n{N} não é perfeito.")