N, asvogas, lista_de_letras, vogais, consoantes = int(input("Escolha um número N que representa o tamanho da lista de letras a serem escritas: ")), "aeiou", [], [], []
print("\n* Se nessa lista o número de vogais tiver proporção parecida (entre 0,1823 e 0,2023) com a do alfabeto ( 5/26 ≈ 0,1923) o jogador ganha;\n* Obs: A e a são diferentes e assim por diante.\n\nA seguir, digite as letras desejadas:")

for numero in range(1, N+1):
  letras=str(input().lower())
  lista_de_letras.append(letras)
  if letras in asvogas :
    vogais.append(letras)
  else:
    consoantes.append(letras)
    
proporcao=len(vogais)/len(lista_de_letras)

if 0.1823<=proporcao<=0.2023:
  print("\nVocê ganhou!")
else:
  print("\nVocê perdeu!")
