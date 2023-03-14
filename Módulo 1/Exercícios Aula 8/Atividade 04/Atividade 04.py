n_de_perfis=int(input("| Criação de perfil para rede social |\n\nQual a quantidade de perfis a ser adicionados? "))

if n_de_perfis<0 or n_de_perfis>100:
  print("número inválido")
  
else:
  lista_de_nomes, lista_de_idades, lista_de_amigos = [], [], []
  
  def app(n_de_perfis):
    
    for numero in range(1, n_de_perfis+1):
      global nome, idade, n_de_amigos
      nome, idade, n_de_amigos = str(input("\nDigite o nome: ")), int(input("Digite a idade: ")), int(input("Digite o número de amigos: "))
      lista_de_nomes.append(nome), lista_de_idades.append(idade), lista_de_amigos.append(n_de_amigos)
      
    for x in range(len(lista_de_idades)):
      if lista_de_idades[x]==max(lista_de_idades):
        print("\nDentre os perfis informados, tiramos as seguintes conclusões;\n\nMais velho:", lista_de_nomes[x])
        break
        
    for x in range(len(lista_de_amigos)):
      if lista_de_amigos[x]==max(lista_de_amigos):
        print("Mais popular:", lista_de_nomes[x])
        break
        
  app(n_de_perfis)
