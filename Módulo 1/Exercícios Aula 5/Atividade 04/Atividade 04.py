n, n2, lista, lista2 = int(input("Digite um número inteiro N para que o programa exiba todos os números de 0 até N em ordem crescente e decrescente simultaneamente\n\nInsira o número aqui: ")), 0, [0], [0]

for n in range (0,n):
  n=n+1
  lista.append(n), lista2.append(n)
  lista2.sort(reverse=True)

print("\r")
for n in range(0,n+1):
  print(lista[n], lista2[n])