string1=str(input("A seguir, digite uma string, o programa irá avaliar e retornar se ela é um palíndromo ou não.\n\n* Palíndromo é uma palavra, frase ou número que permanece igual quando lida de trás para diante.\n\nInsira a frase aqui: "))
string1=string1.replace(" ", "")
string1=string1.lower()
strinvertida=(string1[::-1])

def inverte_string(string1):
  global stringvertida
  strinvertida=(string1[::-1])
  stringvertida=strinvertida.replace(" ", "")
  stringvertida=strinvertida.lower()
  
def processa_string(string1):
  if strinvertida==string1:
    print(True)
  else:
    print(False)

print("\r")
inverte_string(string1)
processa_string(string1)
