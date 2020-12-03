'''
Dona Margarida foi ao Hortifruti, ao chegar lá se deparou com a tabela
dos produtos com os seguintes preços : (Tomate = R$ 1.98 kg, Cebola = R$ 1.48 kg,
Maça = R$ 8.49 kg, Banana = R$ 1.99 kg, Alface = R$ 1.59 unidade e Couve = R$ 4.85 unidade).
Utilizando uma única tupla com elementos heterogeneos, mostre uma tabela com código, nome do 
produto e preços por Kg ou unidade (dependendo do produto), após exibir a tabela,
pergunte qual produto irá levar(utilizando o código do produto) e quantos quilos ou unidades
desse produto escolhido, até continuar == n, quando continuar da repetição mostre no final o total gasto na compra. 
Dica: Usar o índice ou contador pode ajudar no código do produto.
'''
horti = ('Tomate', 1.98, 'Cebola', 1.48, 'Maça ', 8.49,
         'Banana', 1.99, 'Alface', 1.59, 'Couve', 4.85)
total = 0
sair = ()
j = 0
print('-'*7, 'Hortifruti', '-'*7)
print('-'*26)
for d in range(0, len(horti)+1):
    if(j != len(horti)):
        print(horti.index(horti[d])+1, horti[j], "\tR$ %.2f" % horti[j+1])
        j += 2
print('-'*50)
while True:
    op = int(input('Qual item deseja comprar, escolha por código: '))
    if op == 1:
        quant = int(input('Quantos kg vai levar? '))
        total += quant*horti[1]
        continuar = str(input('Deseja continuar?(s/n) '))
        if continuar == 'n':
            break
    if op == 2:
        quant = int(input('Quantos kg vai levar? '))
        total += quant*horti[3]
        continuar = str(input('Deseja continuar?(s/n) '))
        if continuar == 'n':
            break
    if op == 3:
        quant = int(input('Quantos kg vai levar? '))
        total += quant*horti[5]
        continuar = str(input('Deseja continuar?(s/n) '))
        if continuar == 'n':
            break
    if op == 4:
        quant = int(input('Quantos kg vai levar? '))
        total += quant*horti[7]
        continuar = str(input('Deseja continuar?(s/n) '))
        if continuar == 'n':
            break
    if op == 5:
        quant = int(input('Quantas unidades vai levar? '))
        total += quant*horti[9]
        continuar = str(input('Deseja continuar?(s/n)'))
        if continuar == 'n':
            break
    if op == 6:
        quant = int(input('Quantas unidades vai levar? '))
        total += quant*horti[11]
        continuar = str(input('Deseja continuar?(s/n)'))
        if continuar == 's':
            break
print('O total gasto no horti foi:', "R$ %.2f" % total)
print('Muito obrigado, volte sempre!')
print('-'*50)
