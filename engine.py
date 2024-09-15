def header(titulo):
  print()
  print(titulo.center(32))
  print()

#
def opcoes(lista):
  cont = 1
  for opc in lista:
      print(f'{cont} - {opc}')
      cont+=1

#mostra lista de produtos
def listarProdutos(lista):
  for item in lista:
      for chave, valor in item.items():
          print(f'{chave} : {valor} ', end=" ")
      print()  

#adiciona item na lista
def adicionarItem(lista):
  produto={}
  produto["Nome"] = str(input('nome do produto:'))
  produto["Preço"] = int(input("preço:"))
  produto["Quantidade"] = str(input("quantidade:"))
  lista.append(produto)

#remove item da lista
def removerItem(lista):
  nome = str(input('nome do produto:'))
  for item in lista:
      if item["Nome"] == nome:
          lista.remove(item)
          print("item removido com sucesso")