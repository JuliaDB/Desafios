# Mensagem de boas-vindas
print('Bem-vindo a Loja da Julia Brancher')

# Entrada dos dados
valor_unidade = float(input('Entre com o valor do produto: '))
quantidade = int(input('Entre com a quantidade do produto: '))

valor_total = valor_unidade * quantidade

# Bloco condicional para obter o desconto
if valor_total < 2500:
    desconto = 0  # Sem desconto para compras abaixo de 2500
elif (valor_total >= 2500) and (valor_total < 6000):
    desconto = 4  # Desconto de 4% para compras entre 2500 e 5999
elif (valor_total >= 6000) and (valor_total < 10000):
    desconto = 7  # Desconto de 7% para compras entre 6000 e 9999
else:
    desconto = 11  # Desconto de 11% para compras acima de 10000

# Cálculo do valor descontado
valor_total_descontado = (valor_total * (100 - desconto)) / 100

# Saída do console
print(f'O valor SEM desconto: R${valor_total:.2f}')  # Valor total sem desconto
print(f'O valor COM desconto: R${valor_total_descontado:.2f}')  # Valor total com desconto
