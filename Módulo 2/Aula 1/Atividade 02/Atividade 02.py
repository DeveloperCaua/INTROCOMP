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
  def perimetro(self):
    perimetro=self.lado1+self.lado2+self.lado3
    print("\nO perímetro do triângulo informado é de: {:.2f}".format(perimetro))
    
umx, umy, umx2, umy2, umx3, umy3 = float(input("| Cálculo de perímetro de um triângulo |\n\n* Para que seja realizado essa conta, será necessário a coordenada dos vértices do triângulo, representadas da seguinte maneira: (x, y).\n\nA seguir. digite X da primeira coordenada: ")), float(input("Agora, digite Y da primeira coordenada: ")), float(input("\nDigite X da segunda coordenada: ")), float(input("Agora, digite Y da segunda coordenada: ")), float(input("\nDigite X da terceira coordenada: ")), float(input("Por final, didigte Y da terceira coordenada: "))
ponto1, ponto2, ponto3 = Ponto(umx, umy), Ponto(umx2, umy2), Ponto(umx3, umy3)
objeto=Triangulo(ponto1, ponto2, ponto3)
objeto.perimetro()
