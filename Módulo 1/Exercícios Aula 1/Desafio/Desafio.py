n1, n2 = float(input("digite seu peso em kilos: ")), float(input("digite sua altura em cm: "))

IMC = n1/(n2*n2)

print("\nAqui está o seu IMC: ", round(IMC, 2))
if IMC <= 18.5:
  print("\nClassificação: Abaixo do peso")
if 18.6 <= IMC <= 24.9:
  print("\nClassificação: Saudável")
if 25.0 <= IMC <= 29.9:
  print("\nClassificação: Peso em excesso")
if 30.0 <= IMC <= 34.9:
  print("\nClassificação: Obesidade grau I")
if 35.0 <= IMC <= 39.9:
  print("\nClassificação: Obesidade grau II")
if IMC >= 40.0:
  print("\nClassificação: Obesidade grau III")