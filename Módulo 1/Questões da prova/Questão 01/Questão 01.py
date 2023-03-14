N, switch, monitor, cadeira_gamer, jogo_de_tabuleiro, camisa_introcomp = float(input("Qual o valor total arrecadado para a compra de um presente? ")), 3000, 1200, 800, 100, 40

if N>=switch:
  sobra=N-switch
  print("\nVocê pode comprar um Switch!\nIrá sobrar: R$ {:.2f}".format(sobra))
  
elif N<switch and N>=monitor:
  sobra=N-monitor
  print("\nVocê pode comprar um Monitor!\nIrá sobrar: R$ {:.2f}".format(sobra))
  
elif N<switch and N<monitor and N>=cadeira_gamer:
  sobra=N-cadeira_gamer
  print("\nVocê pode comprar uma cadeira Gamer!\nIrá sobrar: R$ {:.2f}".format(sobra))
  
elif N<switch and N<monitor and N<cadeira_gamer and N>=jogo_de_tabuleiro:
  sobra=N-jogo_de_tabuleiro
  print("\nVocê pode comprar um jogo de tabuleiro!\nIrá sobrar: R$ {:.2f}".format(sobra))
  
elif N<switch and N<monitor and N<cadeira_gamer and N<jogo_de_tabuleiro and N>=camisa_introcomp:
  sobra=N-camisa_introcomp
  print("\nVocê pode comprar uma camisa Introcomp\nIrá sobrar: R$ {:.2f}".format(sobra))
  
elif N<switch and N<monitor and N<cadeira_gamer and N<jogo_de_tabuleiro and N<camisa_introcomp:
  print("\nNão tem como comprar algo este ano.\nIrá sobrar: R$ {:.2f}".format(N))
