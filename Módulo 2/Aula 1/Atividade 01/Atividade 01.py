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

umx, umy, umx2, umy2 = float(input("Este programa serve para calcular a distância entre dois pontos.\n\nA seguir, digite o x da primeira coordenada: ")), float(input("Agora, digite o y da primeira coordenada: ")), float(input("\nDigite o x da segunda coordenada: ")), float(input("Agora, digite o y da segunda coordenada: "))
ponto1, ponto2= Ponto(umx, umy), Ponto(umx2, umy2)
distancia=ponto1.distancia(ponto2)
print("\nA distância entre esses dois pontos é de: {:.2f}".format(distancia))
