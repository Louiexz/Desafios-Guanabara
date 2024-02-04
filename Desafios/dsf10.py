#desafio 10
money = int(input('\033[0;37mQuanto dinheiro voce tem na carteira? R$\033[m'))
dollar = money / 5.22
euro = money / 5.50
print(f'\033[0;33mVoce tem R${money}, que dá em:\033[m\n Dólar: {dollar}\n Euro: {euro}')