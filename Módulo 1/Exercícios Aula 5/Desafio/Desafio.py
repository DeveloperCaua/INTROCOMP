lista, lista2, lista3, numero = [], [], [], (input("| Verificação de Ordem (crescente) |\n\n* O programa irá receber valores númericos até que seja digitado '.'\n\nA seguir, digite os números desejados:\n"))
lista.append(numero), lista2.append(numero), lista3.append(numero)

while numero!=".":
  numero=(input())
  lista.append(numero), lista2.append(numero), lista3.append(numero)
lista.remove("."), lista2.remove("."), lista3.remove(".")

for i in range(len(lista)):
  lista[i] = float(lista[i])
for i in range(len(lista2)):
  lista2[i] = float(lista2[i])
for i in range(len(lista3)):
  lista3[i] = float(lista3[i])
  
lista2.sort()
if lista==lista2:
  print("\nA lista está em ordem crescente.\n\n", lista)
else:
  lista.sort(), print("\nA lista não esta em ordem crescente.\n\nEm ordem:", lista), lista3.reverse(), print("\nOriginal:", lista3)
