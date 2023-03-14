gcelsius=int(input("| Controle de temperatura do processador |\n\nDigite, a seguir, a temperatura, em graus Celsius, de seu computador: "))

if gcelsius>75: 
  print("\nSuperaquecimento!")
elif gcelsius<35:
    print("\nCheque o hardware.")
else:
    print("\nTemperatura normal.")