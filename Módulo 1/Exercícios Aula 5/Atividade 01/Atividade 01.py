idade, tempo_de_serviço = int(input("| Cálculo de aposentadoria |\n\nQual a sua idade? ")), int(input("Qual o seu tempo de serviço? "))

if idade>=65 or tempo_de_serviço>=30 or (idade>=60 and tempo_de_serviço>=25):
  print("\nPode se aposentar!")
else:
  print("\nNao pode se aposentar ainda!")
