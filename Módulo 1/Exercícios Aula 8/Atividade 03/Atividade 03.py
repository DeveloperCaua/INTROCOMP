n_de_CPF=int(input("| PROGRAMA DE VERIFICAÇÃO DE CPF |\n\nQuantos CPF's serão verificados? "))
print("\nA seguir, digite o(s) CPF(s) para análise:\n")

for numero in range(1, n_de_CPF+1):
  
  A, B, C, D, E, F, G, H, I, J, K=(input().replace(" ", ""))
  A,B,C,D,E,F,G,H,I,J,K = int(A), int(B), int(C), int(D), int(E), int(F), int(G), int(H), int(I), int(J), int(K)
  J_teste=10*A+9*B+8*C+7*D+6*E+5*F+4*G+3*H+2*I
  J_teste2=J_teste%11
  
  if J_teste2==0 or J_teste2==1:
    J2=0
    
  if J_teste2>=2 and J_teste2<=10:
    J2=11-J_teste2
    
  K_teste=11*A+10*B+9*C+8*D+7*E+6*F+5*G+4*H+3*I+2*J
  K_teste2=K_teste%11
  
  if K_teste2==0 or K_teste2==1:
    K2=0
    
  if K_teste2>=2 and K_teste2<=10:
    K2=11-K_teste2
    
  if J==J2 and K==K2:
    print("CPF verificado!\n")
    
  else:
    print("CPF incorreto!\n")