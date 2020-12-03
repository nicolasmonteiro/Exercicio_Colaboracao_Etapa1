
'''
Angelino mora em Recife e está planejando viajar para os estados que fazem fronteira com Pernambuco, para isso decidiu fazer uma tabela com esses estados e capitais.
Faça um dicionário para cada estado e insira dentro de uma lista. Cada dicionário deve incluir: Estado e Capital.
Imprima na tela os Estados que fazem fronteira com Pernambuco e suas respectivas capitais utilizando lista e dicionário.
Alagoas - Maceió
Bahia - Salvador
Ceará - Fortaleza
Paraíba - João Pessoa
Piauí - Teresina
'''

fronteiraPE = []
Estado1 = {'Estado': 'Alagoas', 'Capital': 'Maceió'}
Estado2 = {'Estado': 'Bahia', 'Capital': 'Salvador'}
Estado3 = {'Estado': 'Ceará', 'Capital': 'Maceió'}
Estado4 = {'Estado': 'Paraíba', 'Capital': 'João Pessoa'}
Estado5 = {'Estado': 'Piauí', 'Capital': 'Teresina'}
fronteiraPE.append(Estado1)
fronteiraPE.append(Estado2)
fronteiraPE.append(Estado3)
fronteiraPE.append(Estado4)
fronteiraPE.append(Estado5)
print('Estados que fazem fronteira com Pernambuco e suas capitais')
for c in (fronteiraPE):
    # Forma alternativa imprimindo direto da lista.
    # print(fronteiraPE[c])
    for k, v in c.items():
        print(k, '-', v)
print('-'*10, 'Boa viagem!', '-'*10)
