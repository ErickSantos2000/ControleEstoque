from engine import *

from data import listaProdutos

while True:
    header("supermercado V.1")

    opcoes(['lista de produtos ', 'adicionar produto', 'remover produto', 'sair'])

    opc = int(input('qual opção deseja:'))


    if opc == 1:
        header("lista de produtos")
        listarProdutos(listaProdutos)
      
    elif opc ==2:
        adicionarItem(listaProdutos)
      
    elif opc == 3:
        removerItem(listaProdutos)

    else:
        break