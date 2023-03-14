c1, c2, c3, c4, y, y_anterior, ponto_maximo, ponto_minimo, subindo, descendo, primeira_vez = int(input("A seguir, digite quatro números decimais representando os coeficientes de uma função, na seguinte ordem:\n\nc1*x3 + c2*x2 + c3*x + c4.\n\nDigite o primeiro número decimal: ")), int(input("Digite o segundo número decimal: ")), int(input("Digite o terceiro número decimal: ")), int(input("Digite o quarto número decimal: ")), 0, 0, None, None, False, False, True

for x in range (-10, 11):
  y_anterior=y
  y=c1*x**3+c2*x**2+c3*x+c4
  
  if not primeira_vez:
    if not subindo and not descendo:
      if y>y_anterior:
        subindo=True
      else:
        descendo=True
    else:
      if subindo and y<y_anterior:
        ponto_maximo=x-1
        subindo=False
        descendo=True
    if descendo and y>y_anterior:
        ponto_minimo=x-1
        subindo=True
        descendo=False
      
  else:
    primeira_vez = False   
    
print("\r")    
if ponto_maximo==None:
  print("Não existe pico máximo.")
  
else:
  print("Existe pico em, aproximadamente, x = ", ponto_maximo)
  
if ponto_minimo==None:
  print("Não existe vale.")
  
else:
  print("Existe vale em, aproximadamente, x =", ponto_minimo)