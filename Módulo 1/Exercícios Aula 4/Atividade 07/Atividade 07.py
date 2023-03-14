numero, anterior, proxima, soma, lista = int(input("Dado um número inteiro, será feito uma lista com essa quantidade de números na sequência de Fibonacci.\n\nDigite o número que deseja: ")), 0, 1, 1, []

for numero in range(0,numero):
  lista.append(anterior)
  soma=proxima+anterior
  anterior=proxima
  proxima=soma

print("\n", lista)