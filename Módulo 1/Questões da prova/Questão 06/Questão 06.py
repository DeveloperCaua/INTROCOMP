def nossa_ord( umaLetra ):
  return ord(umaLetra.upper())-65
  
def progragra_principal():
  nome= input("A seguir, digite um nome sem espaços: ").upper() 
  if nome.isalpha() :  
    valorTotal = 0   
    for letra in nome :
      valor = nossa_ord(letra)
      valorTotal = valorTotal * 26 + valor
    print("\nEste é o inteiro na base alfabética:",  valorTotal)
  else: 
    pass

print("Este é um programa que calcula qual é o número na base 10 que corresponde a uma palavra usando uma base alfabética onde o valor de ’a’ = 0 e ’z’ = 25. Dessa forma:\n\n* Victor_alfabética = 21 ∗ 26^5 + 8 ∗ 26^4 + 2 ∗ 26^3 + 19 ∗ 26^2 + 14 ∗ 26^1 + 17 ∗ 26^0\n* Obs: letras maiúsculas tem mesma pontuação na escala alfabética, ou seja, ’a’ = 0 e ’A’ = 0\n")    
progragra_principal()
