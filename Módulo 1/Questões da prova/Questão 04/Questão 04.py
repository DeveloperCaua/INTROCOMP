lista_de_VIP, lista_de_NORMAL, ingressos= [], [], str(input("Digite quantos ingressos forem necessários, informando sempre se ele é VIP ou NORMAL (em caixa alta), para que seja feito a estimativa de ingressos.\n\nDigite o(s) ingresso(s) a seguir:\n"))

while ingressos!="FIM":
  if ingressos=="NORMAL":
    lista_de_NORMAL.append(ingressos)
  elif ingressos=="VIP":
    lista_de_VIP.append(ingressos)
  else:
    print("\nComando", ingressos, "nao existe!")
  ingressos=str(input())
len(lista_de_VIP)
len(lista_de_NORMAL)
print("\nFoi(ram) contado(s)", len(lista_de_NORMAL),"ingresso(s) normal(is) e", len(lista_de_VIP),"VIP(s)!")
