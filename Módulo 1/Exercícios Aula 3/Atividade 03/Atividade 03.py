nota1, nota2, nota3 = float(input("| Calculadora de média escolar (para três notas) |\n\nDigite a primeira nota: ")), float(input("Digite a segunda nota: ")), float(input("Digite a terceira nota: "))
soma=nota1+nota2+nota3

media=soma/3
if media>=7 and media<8:
  print("\nAluno Aprovado!\nCertificado Bronze\nMédia igual a:", round(media, 2))
elif media>=8 and media<9:
    print("\nAluno Aprovado!\nCertificado Prata\nMédia igual a:", round(media, 2))
elif media>=9 and media<=10:
    print("\nAluno Aprovado!\nCertificado Ouro\nMédia igual a:", round(media, 2))
else:
  print("\nAluno Reprovado!")