"""
1. crie três variáveis, some seus valores, e imprima na tela
"""
x, y, z = 1, 2, 3
soma=x+y+z
print(soma)
print("\n ----------------------------------------------- \n")
"""
2. crie três variáveis, multiplique o valor da primeira por 2, some esse resultado com as duas outras variáveis, e imprima o resultado desta última operação.
"""

x, y, z = 2, 4, 6
multiplicacao= x*2
print("A multiplicação é igual a:",multiplicacao)

resultado=multiplicacao+y+z
print("O resultado final é:", resultado)
print("\n ----------------------------------------------- \n")

"""
3. verifique se um dado número é negativo.
"""
wvalor = int( input("Digite um valor para eu testar se é negativo ou não: "))
print("\nVocê digitou o valor =",wvalor)
if(wvalor<0):
    print("Este valor é negativo.")
else:
    print("Este valor não é negativo.")
print("\n ----------------------------------------------- \n")

"""
4. verifique se um dado número é par ou ímpar.
"""
wvalor=int( input("Digite um valor para eu testar se e ímpar ou par: "))

print("\nVocê digitou: ", wvalor)
if(wvalor %2) ==0:
  print("Este número é par.")
else:
  print("Este número é ímpar.")
print("\n ----------------------------------------------- \n")

"""
5. incremente o valor de uma variável de 1 até 10.
"""
a=1
while(a<=10):
  print(a)
  a=a+1
print("\n ----------------------------------------------- \n")

"""
6. some 10 números apresentados dados como entrada.
"""
print("A seguir, digite dez números, um por vez, para que seja feita a soma deles")
a=10
soma=0
while(a>=1):
  wnumero = int(input("\nFaltam "+str(a)+", Informe um número: "))
  a=a-1
  soma=soma+wnumero
print("\nA soma dessas variáveis da um total de:", soma)