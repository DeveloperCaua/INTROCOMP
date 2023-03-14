tabuada=int(input("| Tabuada de um número N qualquer |\n\nA seguir, digite um número N, o programa irá retornar a tabuada de N: "))
for count in range(10):
    print("\n%d * %d = %d" % (tabuada, count+1, tabuada*(count+1)) )
