nome_da_heroina, numero_de_poder_heroina,  vilao = [], [], input("Este é um jogo sobre a série Sailor Moon!\n\n* Objetivo: Derrotar o vilão utilizando as heroínas;\n* Cada linha de entrada possui o nome composto do personagem e depois o valor de seu ataque, exemplo: Sailor Mars 300;\n* O primeiro nome a ser lido é o do vilão;\n* Todas as Sailor Senshi possuem 'Sailor' como a primeira parte do seu nome;\n* Para terminar a leitura, será utilizado '.'.\n\n")

posicao2=vilao.split(" ")
nome_do_vilao=posicao2[0]+ " "+posicao2[1]
poder_do_vilao=int(posicao2[2])
heroina=input()

while heroina!=".":
  posição=heroina.split(" ")
  nome_da_heroina.append(posição[0]+" "+posição[1])
  numero_de_poder_heroina.append(int(posição[2]))
  heroina=input()
  
if sum(numero_de_poder_heroina)>poder_do_vilao:
  print("As Sailor Senshi ganharam!")
  for japonezinha in (nome_da_heroina):
    print(japonezinha)
    
elif sum(numero_de_poder_heroina)<=poder_do_vilao:
  print(nome_do_vilao, "ganhou!")
