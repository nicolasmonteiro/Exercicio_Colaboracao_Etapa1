
'''
Um grupo de alunos da área de saúde decidiu criar um mini quiz pra conscientizar as pessoas pra melhorar seus hábitos e sua saúde.
Eles não sabem quantos pessoas irão participar da pesquisa. As perguntas são as seguintes: "Está se alimentando com alimentos
saudáveis?", "Está bebendo água suficiente? ","Está dormindo o suficiente? ", "Vai ao médico anualmente? ", "Pratica exercícios físicos
regularmente?" Utilize as perguntas dentro de uma lista.
Se a resposta for sim para duas perguntas ou menos, exiba a seguinte mensagem: "Você está deixando a desejar bastante, cuide mais de sua saúde!"
Se a resposta for sim para três perguntas exiba a seguinte mensagem: "Está ficando preocupante, mas ainda há tempo pra melhorar seus hábitos!"
Se a resposta for sim para quatro perguntas exiba a seguinte mensagem: "Está indo bem, mas pode melhorar!"
Se a resposta for sim para cinco perguntas exiba a seguinte mensagem: "Parabéns por se esforçar em manter uma boa saúde!"
Quando finalizar as 5 perguntas da lista, perguntar se  deseja fazer outra pesquisa, 
se a resposta for 'não' exiba a quantidade de pessoas pesquisadas e sai do loop.
    '''
cont = 0
while True:
    cont += 1
    print('-'*20 + 'Pesquisa sobre saúde' + '-'*20)
    print('-'*20 + "Responda com s ou n", '-'*20)
    perguntas = ["Está se alimentando com alimentos saudáveis? ---> ", "Está bebendo água suficiente?---> ",
                 "Está dormindo o suficiente? ---> ", "Vai ao médico anualmente? ---> ", "Pratica exercícios físicos regularmente? ---> "]

    soma = 0
    i = 0
    while i < len(perguntas):
        print('-'*60)
        resp = input(perguntas[i])
        print('-'*60)
        if resp == "s":
            soma += 1
        else:
            soma = soma
        i = i + 1

    if soma <= 2:
        print("Você está deixando a desejar bastante, cuide mais de sua saúde! ")
        print('-'*60)
    elif soma == 3:
        print("Está ficando preocupante, mas ainda há tempo pra melhorar seus hábitos!")
        print('-'*60)
    elif soma == 4:
        print("Está indo bem, mas pode melhorar!")
        print('-'*60)
    elif soma == 5:
        print("Parabéns por se esforçar em manter uma boa saúde!")
        print('-'*60)
    print('Obrigado pela sua opinião!')
    print('-'*60)
    repetir = str(input('Deseja fazer uma nova pesquisa (s/n) '))
    print('-'*60)
    if repetir == 'n':
        print('-'*60)
        print('No total foram pesquisadas:', cont, 'pessoa(s).')
        break
