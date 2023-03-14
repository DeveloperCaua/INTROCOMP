from math import sqrt

def calculo_de_distancia(px, py, sx, sy):
  qd = (px-sx)**2 + (py-sy)**2
  return sqrt(qd)
  
primeiro_aluno_x, primeiro_aluno_y, segundo_aluno_x, segundo_aluno_y, terceiro_aluno_x, terceiro_aluno_y, x_professor, y_professor,  perimetro = int(input("Encontre o Marco!\n\nPara que seja completa tal missão insira, a seguir, a sua coordenada.\n\nAluno 01, qual sua posição Ax? ")), int(input("Qual sua posição Ay? ")), int(input("\nAluno 02, qual sua posição Ax? ")), int(input("Qual sua posição Ay? ")), int(input("\nAluno 03, qual sua posição Ax? ")), int(input("Qual sua posição Ay? ")), int(input("\nAgora, insira a coordenada onde o Marco se encontra, qual o valor Ax? ")), int(input("Agora, insira o valor Ay: ")), int(input("\nQual o perímetro preciso?\n\n* O 'perímetro preciso' nada mais é do que o perímetro máximo do triângulo formado pelos alunos 'investigadores' para que a distância seja considerada precisa.\n\n "))

distancia_1=calculo_de_distancia( \
      primeiro_aluno_x,primeiro_aluno_y,\
      segundo_aluno_x, segundo_aluno_y\
      )
distancia_2=calculo_de_distancia(\
      segundo_aluno_x, segundo_aluno_y, \
      terceiro_aluno_x, terceiro_aluno_y\
      )
distancia_3=calculo_de_distancia(\
      primeiro_aluno_x, primeiro_aluno_y,\
      terceiro_aluno_x, terceiro_aluno_y\
      )
distpro1=calculo_de_distancia(\
      primeiro_aluno_x, primeiro_aluno_y,\
      x_professor, y_professor)
distpro2=calculo_de_distancia(\
      segundo_aluno_x, segundo_aluno_y,\
      x_professor, y_professor)
distpro3=calculo_de_distancia(\
      terceiro_aluno_x, terceiro_aluno_y,\
      x_professor, y_professor)
soma_alunos=distancia_1+distancia_2+distancia_3
soma_professor_aluno=distpro1+distpro2+distpro3

if distpro1==distpro2==distpro3:
  print("\nO Marco está bem perto! :D")
elif soma_alunos>soma_professor_aluno:
  if perimetro<soma_alunos:
    print("\nO Marco pode estar perto! :)")
  else:
    print("\nO Marco está bem perto! :D")
else:
  print("\nNão sabemos onde está o Marco :(")
