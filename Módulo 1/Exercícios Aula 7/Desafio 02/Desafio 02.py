figurinhas_faltantes, n_de_figurinhas, figurinhas_compradas, lista = int(input("Digite o número total de espaços no álbum de figurinhas: ")), int(input("Digite o número de figurinhas compradas: ")), int(input("\nA partir desses dados, comece a digitar o número de cada figurinha comprada.\n\nDigite os números a seguir:\n")), []
lista.append(figurinhas_compradas)

while len(lista)!=n_de_figurinhas:
  figurinhas_compradas=int(input())
  lista.append(figurinhas_compradas)
  
if not 1<=figurinhas_faltantes<=100 or not 1 <= n_de_figurinhas <= 300 or not 1 <= figurinhas_compradas <= figurinhas_faltantes:
  print("Esses números não são válidos.")
else:
  lista_sem_repetidos = []
  for i in lista:
    if i not in lista_sem_repetidos:
      lista_sem_repetidos.append(i)
  quantidade_figurinhas_repetidas = len(lista) - len(lista_sem_repetidos)

  figurinhas_faltantes=figurinhas_faltantes-len(lista_sem_repetidos)
  print("\nFaltam {} figurinha(s) para completar o album.".format(figurinhas_faltantes))
  print("Tem {} figurinha(s) repetida(s).".format(quantidade_figurinhas_repetidas))
