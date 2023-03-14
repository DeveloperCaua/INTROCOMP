N, lista = int(input("Qual será o tamanho da sua lista? ")), []
print("\nAgora, digite os valores que irão compor essa lista: ")

def calculo(N):
  for numero in range(1, N+1):
    numero=int(input())
    lista.append(numero)
    
  media=sum(lista)/N
  print("\nO maior número da lista é {}, o menor é {} e a média é {:.2f}.".format(max(lista), min(lista), media))
calculo(N)
