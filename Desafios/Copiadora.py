# Mensagem de boas-vindas
print('Bem-vindo a Copiadora de Julia Brancher')
print('\n')

# Seleção de opções de serviços desejados
def escolha_servico():

    while True:
        print('DIG - Digitalização')
        print('ICO - Impressão Colorida')
        print('IPB - Impressão Preto e Branco')
        print('FOT - Fotocópia')

        servico = input('Entre com o tipo de serviço desejado: ')
        servico = servico.upper()

        if servico == "DIG": #Digitalização
            return 1.10
        elif servico == "ICO": #Impressão Colorida
            return 1.00
        elif servico == "IPB": #Impressão Preto e Branco
            return 0.40
        elif servico == "FOT": #Fotocópia
            return 0.20
        else:
            print('Escolha inválida, entre com o tipo do serviço novamente\n')

# Número de páginas solicitadas com/sem desconto
def num_pagina():
    quantidade = 0
    desconto = 0
    while True:
        try:
            quantidade = int(input('Entre com o número de páginas: '))
            if quantidade < 20:
                desconto = 0
                break
            elif (quantidade >= 20) and (quantidade < 200):
                desconto = 15
                break
            elif (quantidade >= 200) and (quantidade < 2000):
                desconto = 20
                break
            elif (quantidade >= 2000) and (quantidade < 20000):
                desconto = 25
                break
            else:
                print(
                    f'Não aceitamos tantas páginas de uma vez. \nPor favor, entre com o número de páginas novamente.\n')
        except ValueError:
            continue

    return quantidade * (100 - desconto) / 100


# Valor dos serviços extras
def servico_extra():
    print('1 - Encadernação Simples - R$ 15.00')
    print('2 - Encadernação Capa Dura - R$ 40.00')
    print('0 - Não desejo mais nada')

    while True:
        opcao = int(input('Deseja adicionar algum serviço? '))
        if opcao == 1: # Encadernação Simples
            return 15
        elif opcao == 2: # Encadernação Capa Dura
            return 40
        elif opcao == 0: # Não desejo mais nada
            return 0
        else:
            continue

# Pedido total
def main():
    opcao_servico = escolha_servico()
    quantidade = num_pagina()
    valor_extra = servico_extra()

    total = (opcao_servico * quantidade) + valor_extra
    print(f'Total: {total} (serviço: {opcao_servico:.2f} * páginas: {int(quantidade)} + extra: {valor_extra:.2f})')


if __name__ == '__main__':
    main()