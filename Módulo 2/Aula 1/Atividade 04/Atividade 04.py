def verificação(determinante):
  if determinante == 0:
    return False
  else:
    return True

class Ponto:
  def __init__(self, umx , umy):
    self.x = umx
    self.y = umy

  def __str__(self):
    return f"x:{self.x} y:{self.y}"
  
  def distancia(self, outroponto ):
    dx = (self.x - outroponto.x)**2
    dy = (self.y - outroponto.y)**2
    return (dx+dy)**0.5
    
class Triangulo:
  def __init__(self, ponto1, ponto2, ponto3):
    self.lado1=ponto1.distancia(ponto2)
    self.lado2=ponto2.distancia(ponto3)
    self.lado3=ponto1.distancia(ponto3)
    self.determinante=umx*umy2*1 + umy*1*umx3 + 1*umx2*umy3 - (umx3*umy2*1 + umy3*1*umx + 1*umx2*umy)
    ver = verificação(self.determinante)
    if ver is False:
      print("\nERRO! Os pontos dados nao formam um triângulo.")
      self.erro=True
    else:
      self.erro=False
      if self.lado1==self.lado2 and self.lado1==self.lado3 and self.lado2==self.lado3:
        print("\nOs pontos dados formam um triângulo equilátero.")
      elif self.lado1==self.lado2!=self.lado3 or self.lado1==self.lado3!=self.lado2 or self.lado2==self.lado3!=self.lado1:
        print("\nOs pontos dados formam um triângulo isósceles.")
      elif self.lado1!=self.lado2 and self.lado1!=self.lado3 and self.lado2!=self.lado3:
        print("\nOs pontos dados formam um triângulo escaleno.")
  def perimetro(self):
    perimetro=self.lado1+self.lado2+self.lado3
    if self.erro==False:
      print("O perímetro é igual a: {:.2f}".format(perimetro))

  def area(self):
    area=abs(self.determinante*0.5)
    if self.erro==False:
      print("A área é igual a: {:.2f}".format(area))
      
umx, umy, umx2, umy2, umx3, umy3 = float(input("| Cálculo de perímetro ou área de um triângulo |\n\n* Para que seja realizado essa conta, será necessário a coordenada dos vértices do triângulo, representadas da seguinte maneira: (x, y).\n* O programa também irá informar se os pontos são colineares (não formam um triângulo) ou se formam um triângulo, informando também qual o seu tipo.\n\nA seguir. digite X da primeira coordenada: ")), float(input("Agora, digite Y da primeira coordenada: ")), float(input("\nDigite X da segunda coordenada: ")), float(input("Agora, digite Y da segunda coordenada: ")), float(input("\nDigite X da terceira coordenada: ")), float(input("Por final, didigte Y da terceira coordenada: "))

ponto1, ponto2, ponto3 = Ponto(umx, umy), Ponto(umx2, umy2), Ponto(umx3, umy3)
qualcalculo=int(input("\nA seguir, informe qual cálculo será realizado:\n\n* 1-Perímetro;\n* 2- Área.\n\n"))
objeto=Triangulo(ponto1, ponto2, ponto3)

if qualcalculo==1: 
  objeto.perimetro()
elif qualcalculo==2:
  objeto.area()
