import numpy
lista=[]
print("A seguir, digite a quantidade desejada de números inteiros para que seja calculada o produto dos números listados.\n\n* Para encerrar o pedido de números, digite 0.\n")
while True:
  numero=int(input())
  if numero==0:
    break
  lista.append(numero)
if len(lista)>0: 
  produto=numpy.prod(lista)
  print("\nO produto dos números digitados é igual a:", produto)
