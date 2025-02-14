# Mensagem de boas-vindas
print("Bem-vindo a Loja de Gelados da Julia Brancher")
print('----------------------Cardápio-----------------------')
print('---| Tamanho  |    Cupuaçu (CP)  |   Açaí (AC)  | ---')
print('---|    P     |    R$ 9.00       |   R$ 11.00   | ---')
print('---|    M     |    R$ 14.00       |   R$ 16.00  | ---')
print('---|    G     |    R$ 18.00       |   R$ 20.00  | ---')
print('-----------------------------------------------------')

valor_total_pedido = 0
valor_produto = 0

# Bloco condicional para a escolha do sabor e o tamanho
while True:
    while True:
        sabor_escolhido = input('Entre com o sabor desejado (CP/AC): ')
        sabor_escolhido = sabor_escolhido.upper()

        if (sabor_escolhido != 'CP') and (sabor_escolhido != 'AC'):
            print('Sabor inválido. Tente novamente\n')
            continue

        tamanho_escolhido = input('Entre com o tamanho desejado (P/M/G): ')
        tamanho_escolhido = tamanho_escolhido.upper()

        if (tamanho_escolhido != 'P') and (tamanho_escolhido != 'M') and (tamanho_escolhido != 'G'):
            print('Tamanho inválido. Tente novamente\n')
            continue
        else:
            break

    # Obtendo o valor do produto escolhido
    if sabor_escolhido == 'CP':
        if tamanho_escolhido == 'P':
            valor_produto = 9.00
        elif tamanho_escolhido == 'M':
            valor_produto = 14.00
        else:
            valor_produto = 18.00
        print(f'Você pediu um Cupuaçu no tamanho {tamanho_escolhido}: R$ {valor_produto:.2f}')

    if sabor_escolhido == 'AC':
        if tamanho_escolhido == 'P':
            valor_produto = 11.00
        elif tamanho_escolhido == 'M':
            valor_produto = 16.00
        else:
            valor_produto = 20.00
        print(f'Você pediu um Açaí no tamanho {tamanho_escolhido}: R$ {valor_produto:.2f}')

    # Acumulador do pedido total
    valor_total_pedido = valor_total_pedido + valor_produto

    # Verificando se deseja adicionar mais produtos
    continuar_pedido = input('\nDeseja pedir mais alguma coisa? (S/N): ')
    continuar_pedido = continuar_pedido.upper()

    # Se deseja continuar o pedido, retorna para o início do while
    if continuar_pedido == 'S':
        continue
    else:
        print(f'\nO valor total a ser pago: R$ {valor_total_pedido:.2f}')
        break
