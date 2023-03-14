import math
wraio=float(input("A seguir, será calculado o valor da área de um círculo e, em seguida, o raio de um círculo com metade dessa área.\n\nInforme o raio de um círculo: "))

Area=math.pi*wraio**2 
Area2=Area/2
wraiometade=math.sqrt(Area2/math.pi)
print("\nO valor da área desse círculo é igual a: {:.2f}\nJá o valor do raio de um círculo com metade dessa área é igual a: {:.2f}".format(Area, wraiometade))