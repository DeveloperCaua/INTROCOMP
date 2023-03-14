xnumero, ynumero, znumero = float(input("| Calculadora de média para três pesos (notas) |\n\nDigite a nota 01: ")), float(input("Digite a nota 02: ")), float(input("Digite a nota 03: "))
soma=xnumero+ynumero+znumero
media=soma/3
print("\nA média do aluno é: {:.1f}".format(media))
