import math
x, contador, lista_altura, area = float(input("Dê, como entrada, um número real representando a largura da base de um retângulo. Considere que todas as entradas podem ser escritas da forma 5/k, onde k é um número inteiro positivo: ")), 0, [], []

while (contador<5):
  contador=contador+x
  if contador>5:
    break
  else:
    y=math.sqrt(contador)
    lista_altura.append(y)
    
for a in range(len(lista_altura)):
  v=lista_altura[a]*x
  area.append(v)
  
resposta=sum(area)
print("\nEsta é a soma das áreas de todos os retângulos formados pela soma de Riemann, com 3 casas decimais: {:.3f}".format(resposta))