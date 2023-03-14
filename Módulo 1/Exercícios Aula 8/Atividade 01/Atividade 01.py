n_de_suspeitos, lista, suspeitos, cores, lista_de_suspeitos = int(input("Olá! Estou aqui para encontrar o culpado que está comendo suas cenouras...\n\nA seguir, me diga quantas pessoas estão envolvidas no caso: ")), [], [], [], []
print("\nCerto, agora irei precisar do nome e a cor dos dentes de cada suspeito.\n\nInsira aqui, um por vez, esses dados:\n")

def analise(n_de_suspeitos):
  for numero in range(1, n_de_suspeitos+1):
    suspeitos_e_cor_dos_dentes=str(input())
    suspeitos=suspeitos_e_cor_dos_dentes.split(" ")
    lista_de_suspeitos.append(suspeitos[0])
    cores.append(suspeitos[1])
  for x in range(len(cores)):
    if cores[x]=="Laranja":
      print("\nO culpado por estar comendo suas cenouras é:", lista_de_suspeitos[x])
    else:
      continue

analise(n_de_suspeitos)