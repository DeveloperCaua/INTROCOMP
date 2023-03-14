A, B, C = int(input("| Teorema de Tales |\n\n*  O Teorema de Tales diz que: a razão dos segmentos criados por duas retas paralelas em duas retas transversais, são proporcionais.\n\nEntão, a seguir, escreva os valores de A, B e C, para que seja descoberto o valor de D por meio deste teorema.\n\nEscreva o valor de A: ")), int(input("Escreva o valor de B: ")), int(input("Escreva o valor de C: "))
(0 < A, B, C <= 10000)
D = B * C / A
print("\nAqui está o valor de D: {:.2f}".format(D))