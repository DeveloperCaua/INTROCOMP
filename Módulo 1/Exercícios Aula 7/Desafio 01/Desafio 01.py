string_principal, string_secundaria = str(input("A seguir, digite duas strings, o programa ira avaliar e retornar se uma é a subsequência da outra.\n\nDigite a primeira string: ")), str(input("Digite a segunda string: "))

string_principal=string_principal.replace(" ", "")
string_principal=string_principal.lower()
string_secundaria=string_secundaria.replace(" ", "")
string_secundaria=string_secundaria.lower()

def eh_subsequencia(string_principal, string_secundaria):
  global string_temporaria
  for i in range(len(string_secundaria)):
    string_temporaria=string_principal.replace(string_secundaria[i],"",1)
    if string_temporaria==string_principal:
      print(False)
      exit()
    else:
      string_principal=string_temporaria
  print(True)

print("\r")
eh_subsequencia(string_principal, string_secundaria)