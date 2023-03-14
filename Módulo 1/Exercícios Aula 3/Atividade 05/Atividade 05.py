a, b, c = float(input("A seguir, escreva os coeficientes A, B e C de uma equação do segundo grau.\n\nDigite o valor de A: ")), float(input("Digite o valor de B: ")), float(input("Digite o valor de C: "))
delta=b**2-4*a*c

if delta<0:
  print("\nEssa equação só possui raízes complexas (Delta menor que zero).")
elif delta==0:
  print("\nEssa equação só possui uma raiz real (Delta igual a zero).")
else:
  print("\nEssa equação só possui duas raízes reais (Delta maior que zero).")