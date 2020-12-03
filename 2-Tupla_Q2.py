'''
Mathias está ansioso para saber qual vai ser o game do ano no evento The Game Awards, esse evento é considerado o 'Oscar do videogame'.
Os indicados são : The Last of Us Part 2, Animal Crossing:New Horizon,Final Fantasy 7 Remake,Ghost of Tsushima e Hades.
Para se preparar para o evento decidiu jogar todos os jogos indicados e depois dará uma nota para cada jogo. 
Utilizando tupla faça uma tabela com os jogos a serem jogados e peça a nota de cada jogo, no final mostre o jogo com a maior nota e a menor nota. 
Tanto a maior nota quanto a menor deve ter o nome do jogo relacionado. 
'''
jogos = ('The Last of Us Part 2', 'Animal Crossing:New Horizon',
         'Final Fantasy 7 Remake', 'Ghost of Tsushima', 'Hades')
cont = 0
maior = 0
menor = 999
print('-'*5, 'Jogos indicados a game do ano', '-'*5)
for j in range(0, len(jogos)):
    print(jogos.index(jogos[j]) + 1, jogos[j])
for i in range(0, len(jogos)):
    print('-'*40)
    print(jogos[cont])
    nota = int(input('Qual nota do jogo? '))
    print('-'*40)
    cont += 1
    if nota > maior:
        melhor = i
        maior = nota
    if nota < menor:
        menor = nota
        pior = i
print('A maior nota foi', maior, 'do jogo', jogos[melhor])
print('A menor nota foi', menor, 'do jogo', jogos[pior])
