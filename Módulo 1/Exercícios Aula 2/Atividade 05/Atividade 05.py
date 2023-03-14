wstring, wcomeco = str(input("Escreva uma string qualquer: ")), int(input("\nAgora, a partir do número N, o programa irá printar as cinco primeiras letras seguinte, começando por N.\n\nEscreva um número N qualquer: "))
wfim = wcomeco + 5
print("\nAs seguintes letras se encontram a partir de N: '", wstring[wcomeco:wfim], "'")