receita, dispesas = float(input("| Calculadora de lucro financeiro/empresarial |\n\nA seguir, digite a receita de sua empresa: ")), float(input("A seguir, digite a despesa de sua empresa: "))
resultado=receita-dispesas
if resultado>0:
  print("\nSua empresa obteve o lucro de R$ " "{:.2f}""!".format(resultado))
else:
  print("\nSua empresa obteve o prejuizo de R$ " "{:.2f}""!".format(abs(resultado)))