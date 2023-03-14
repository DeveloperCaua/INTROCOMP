wcaracter, wtemperatura, wconversao = input("A seguir, digite um dos seguintes caracteres:\n\n* C, caso queira transformar Celsius para Fahrenheit;\n* F, caso queira transformar Fahrenheit para Celsius.\n\n"), float(input("\nDigite a temperatura, de acordo com o caracter escolhido: ")), 0

if wcaracter== "C"or wcaracter=="c":
  wconversao=(wtemperatura*9/5)+32
  print("\nO valor da conversão de Celsius para Fahrenheit é igual a: {:.1f}".format(wconversao))
elif wcaracter=="F" or wcaracter=="f":
  wconversao=(wtemperatura-32)/1.8
  print("\nO valor da conversão de Fahrenheit para Celsius é igual a: {:.1f}".format(wconversao))