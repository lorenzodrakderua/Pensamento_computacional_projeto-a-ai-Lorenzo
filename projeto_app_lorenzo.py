'''

CRUD

Açai

um aplicativo fast food, onde voce pode pedir sua sobremesa, personalizar o seu açai , efetuar o seu 
pagamento e acompanhar o seu pedido

'''


print('\== site açai==')
print('1. fazer o pedido')
print('2. ver meus pedidos ')
print('3.mudar rapido ')
print('4. cancelar pedido')
print('5.relátorio do pedido')
print('6.sair')

while True:

    escolha_cliente = input('o que voce deseja fazer?')

    if escolha_cliente == '1':
        print('vamos começar o seu pedido')
        nome_cliente = input('descreva como voce quer o seu açai e o tamanho dele:')
        pedido_cliente = input('descreva como voce quer o seu açai e o tamanho dele:')

    elif escolha_cliente == '2':
        print('açai está seus pedidos:')

    elif escolha_cliente == '3':
        print('oque voce deseja mudar no seu pedido?')

    elif escolha_cliente == '4':
        print('seu pedidod foi cancelado!')

    elif escolha_cliente == '5':
         print('aqui esta o relátorio do seu pedido.')

    elif escolha_cliente == '8':
        print('saindo do site. até logo')
        break

    else:
     print('opção invalida. por favor tente novamente.')