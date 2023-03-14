class Carro:
  def __init__(self, Vmedia, consumo, CdoTanque, QAdoTanque):
    self.Vmedia=Vmedia
    self.Consumo=consumo
    self.CdoTanque=CdoTanque
    self.QAdoTanque=QAdoTanque

  def Viajar(self, QuantKilometros):
    self.tempo=QuantKilometros/self.Vmedia
    self.combustivelgasto=QuantKilometros/self.Consumo
    self.QAdoTanque=self.QAdoTanque-self.combustivelgasto
    print("\nO carro andou {:.2f} km em {:.2f} horas e gastou {:.2f} litros de combustível. O carro agora possui {:.2f} litros de combustível.\n".format(QuantKilometros, self.tempo, self.combustivelgasto, self.QAdoTanque))

  def Abastecer(self, QuantCombustivel):
    self.QAdoTanque=self.QAdoTanque+QuantCombustivel
    print("\nO carro foi abastecido com {:.2f} litros. O tanque agora esta com {:.2f} litros de combustível.\n".format(QuantCombustivel, self.QAdoTanque))

  def Completar(self):
    if self.QAdoTanque>self.CdoTanque:
      self.QAdoTanque=self.CdoTanque
    self.QuantNecessaria=self.CdoTanque-self.QAdoTanque
    self.QAdoTanque = self.CdoTanque
    print("\nO carro foi abastecido com {:.2f} litros e esta com o tanque cheio!\n".format(self.QuantNecessaria))

print("| Programa de apoio ao motorista |\n\n* Informe, um por vez, a velocidade média, consumo e capacidade do tanque de seu carro.\n")

combustivelatual, AposAbastecer, Vmedia, consumo, CdoTanque = 0, 0, float(input()), float(input()), float(input())
QAdoTanque=CdoTanque

objeto=Carro(Vmedia, consumo, CdoTanque, QAdoTanque)
print("\nAgora, com os devidos dados informados, escolha uma opção:\n\n* Viaja: Será necessário informar a quantidade de quilômetros da viajem como parâmetro. O programa irá informar o tempo gasto para realizar essa kilometragem, o combustível gasto e o quanto de gasolina que sobrou no tanque;\n\n* Abastece: Deve ser informado a quantidade, em litros, que o carro recebeu de gasolina. O programa irá retornar a quantidade de litros presente no tanque e, caso ele esteja cheio, será informado;\n\n* Completa: O programa irá informar a quantidade de litros que falta para completar o tanque, realizando a ação de abastecimento;\n\n* Encerra: Encerra o programa.\n")

while True:
  ação=str(input())
  if ação=="Viaja":
    QuantKilometros=int(input())
    objeto.Viajar(QuantKilometros)
  elif ação=="Abastece":
    QuantCombustivel=int(input())
    objeto.Abastecer(QuantCombustivel)
  elif ação=="Completa":
    objeto.Completar()
  elif ação=="Encerra":
    break
