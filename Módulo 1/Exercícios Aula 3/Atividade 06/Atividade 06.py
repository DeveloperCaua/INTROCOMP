wc, wc1, wc2, wc3, wc4 = int(input("| Técnicas de podagem para sua árvore (dependendo das características dela) |\n\nA árvore possui tronco fino? \n")), int(input("A raiz é externa? \n")), int(input("A árvore está em época de fruto? \n")), int(input("A árvore está doente? \n")), int(input("A árvore possui trepadeiras? \n"))

if wc4 == 1:
  wc4a=int(input("A trepadeira é jovem? \n"))
wc5=int(input("A árvore possui plantas ornamentais? \n"))
  
if wc==1:
  print("\nRetirar galhos mortos;\n")
if wc1==1:
  print("Aterrar raizes;\n")
if wc2==1:
  print("Cuidado com os brotos;\n")
if wc3==1:
  print("Corte na região afetada;\n")
if wc4==1 and wc4a==1:
  print("Podar;\n")
elif wc4==1 and wc4a==0:
  print("Deixa;\n")
if wc5==1:
  print("Corte delicado com tesoura;")
