n_de_jogadores,lista_de_posições, lista_de_jogadores, numero_de_partidas, numero_de_gols, numero_de_assist = int(input("Olá! Siga as seguintes instruções para a utilização do programa:\n\n* O programa foi criado para encontrar jogadores que se encaixam com as características necessárias para determinado time;\n* digite um inteiro N, que representará o número de linhas;\n* Cada linha contém um identificador da posição (sendo M = meio-campista, A = atacante, Z = zagueiro e G = goleiro), um nome de jogador e três inteiros (número de partidas, gols e assistências).\n\nA seguir, digite o número N de linhas: ")), [], [], [], [], []

print("\nAgora, uem cada linha, digite a posição, nome do jogador, número de partidas, gols e assistências:\n")
for numero in range(1, n_de_jogadores+1):
  jogador=(input())
  posição=jogador.split(" ")
  lista_de_posições.append(posição[0]), lista_de_jogadores.append(posição[1]), numero_de_partidas.append(posição[2])
  
  for i in range (len(numero_de_partidas)):
    numero_de_partidas[i]=int(numero_de_partidas[i])
  numero_de_gols.append(posição[3])
  
  for i in range (len(numero_de_gols)):
    numero_de_gols[i]=int(numero_de_gols[i])
  numero_de_assist.append(posição[4])
  
  for i in range (len(numero_de_assist)):
    numero_de_assist[i]=int(numero_de_assist[i])

print("\nFoi(foram) contratado(s), o(s) seguinte(s) jogador(es):\n")
for x in range(len(lista_de_posições)):
  if lista_de_posições[x]=="M":
    media_de_assist=numero_de_assist[x]/numero_de_partidas[x]
    if media_de_assist>0.3:
      print("M -",lista_de_jogadores[x])
      
for x in range(len(lista_de_posições)):
  if lista_de_posições[x]=="A":
    media_de_gols=numero_de_gols[x]/numero_de_partidas[x]
    if media_de_gols>0.8:
      print("A -",lista_de_jogadores[x])
