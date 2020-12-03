'''
Josemar trabalha numa revendedora de carros usados, tem 4 carros na empresa,
a cada carro vendido ele ganha 0,5 % (0,005 em decimal) de comissão:
Os carros são:
1-Classic -----(R$17.000)
2-Onix ----- (R$45.000)
3-Palio ----- (R$15.000
4-Logan -----(R$40.000)
Utilizando lista composta guarde o nome e preço dos carros. Para vender o carro mostre uma tabela com os carros e os preços.
A pessoa escolhe o carro pelo código, o código vai de 1 a 4, do Classic ao Logan, respectivamente. A cada carro vendido deve
adicionar esse carro numa nova lista chamada carrosvendidos. Quando o carro for vendido a mensagem do carro vendido deve mudar. 
Por exemplo: Se o carro 1 for vendido a tabela ficará:
'Vendido'
2-Onix ----- (R$45.000)
3-Palio ----- (R$15.000
4-Logan -----(R$40.000)
A venda acaba quando os carros acabarem ou quando a pessoa não quiser continuar.
No final mostre: quantidade de carros restantes(tamanho da lista de carros - tamanho da lista de carros vendidos),quantidade de carros vendidos 
e quanto Josemar lucrou no final em reais.
Dica: Para utilizar o código coloque junte do nome do carro, por exemplo O código aqui é 1.:  '1-Classic'. 
'''
carros = [['1-Classic', 17000], ['2-Onix', 45000],
          ['3-Palio', 15000], ['4-Logan', 40000]]
carrosvendidos = []
josemar = float(0)
'''
print(carros[0][0])
print(carros[1][1])
print(carros[1])
'''
print('-'*5, 'Carros a venda', '-'*5)
for c in carros:
    print(f'{c[0]} ------- R$ {c[1]}')
while True:
    op = int(input('Qual carro irá levar? (Digite o código)'))
    if op == 1:
        josemar += 0.005 * carros[0][1]
        carrosvendidos.append(carros[0:])
        carros[0] = 'Vendido'
    if op == 2:
        josemar += 0.005 * carros[1][1]
        carrosvendidos.append(carros[1:])
        carros[1] = 'Vendido'
    if op == 3:
        josemar += 0.005 * carros[2][1]
        carrosvendidos.append(carros[2:])
        carros[2] = 'Vendido'
    if op == 4:
        josemar += 0.005 * carros[3][1]
        carrosvendidos.append(carros[3:])
        carros[3] = 'Vendido'
    if len(carrosvendidos) == 4:
        break
    continua = str(input('Deseja continuar?(s/n)'))
    if continua == 'n':
        break
    for c in carros:
        print(f'{c[0]} ------- R$ {c[1]}')
print(f'Josemar vendeu: {len(carrosvendidos)} carro(s)')
print('No final sobraram :', len(carros)-len(carrosvendidos), 'carro(s)')
print('Josemar lucrou com as vendas: R$', josemar)
