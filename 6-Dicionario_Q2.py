'''
Alguns amigos sairam para jantar fora nessa noite ficou definido que seria feito um sorteio para quem iria pagar a conta.
Para isso faça um dicionário com os nomes dos amigos e faça um sorteio dentre esses para ver quem vai pagar a conta.

'''
import random
amigos = {}
print('-'*15, 'SORTEIO', "-"*15)
quant = int(input('Quantos amigos vão sair?'))
for c in range(0, quant):
    amigos[c] = str(input('Informe seu nome: '))
sorteio = random.choice(list(amigos.values()))
print(f'Se deu mal, vai ter que pagar hein {sorteio} !')
