n1, n2 = int(input("A seguir, digite um número inteiro entre (-1000 <= num <= 1000) até que o primeiro número seja repetido. Dada a sequência, será retornado o maior número dentro da lista.\n\n")), int(input())

lista=[n1,n2,]
lista.append(n2)
while n1!=n2:
  n2=int(input())
  lista.append(n2)
print("O maior número presente nessa lista é:", max(lista))