segundos=int(input("| Conversor de segundos |\n\nInsira um valor valor em segundos para que seja tranformado em meses, dias, horas, minutos e segundos.\n\nInsira o número aqui: "))

def tempo_de_funcionamento(segundos):
  meses=segundos//2592000
  segundos_rest=segundos%2592000
  dias=segundos_rest//86400
  segundos_rest=segundos%86400
  horas=segundos_rest//3600
  segundos_rest=segundos_rest%3600
  minutos=segundos_rest//60
  segundos_rest=segundos_rest%60
  print("\nMeses:", meses,"\nDias:", dias,"\nHoras:", horas,"\nMinutos", minutos,"\nSegundos:", segundos_rest)
  
tempo_de_funcionamento(segundos)
