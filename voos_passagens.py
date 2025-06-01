import os
from random import randint

def exibe_dados_voo(voo):
    print(f'\033[1mCódigo:\033[m {voo[0]}\n\033[1mCidade de origem:\033[m {voo[1][0]}\n\033[1mCidade de destino:\033[m {voo[1][1]}\n\033[1mQuantidade de escalas:\033[m {voo[1][2]}\n\033[1mValor das passagens:\033[m R${voo[1][3]}\n\033[1mQuantidade de lugares disponíveis:\033[m {voo[1][4]}')

voos = {}
passageiros = {}

passagens = []
voos_disponiveis = []

informacoes = []

if voos != {}:
    for voo in voos.items():
        if voo[1][4] > 0:
            voos_disponiveis.append(voo[0])

os.system('cls' if os.name == 'nt' else 'clear')

print('\n\n\t\033[1m=-=-=-=-= BEM VINDO(A) AO SISTEMA DE CONTROLE DE PASSAGENS AÉREAS =-=-=-=-=\033[m\n\n')
print('O sistema serve para cadastrar e consultar voos e passsageiros e vender e cancelar passagens\n')
input('\n\t<< Tecle Enter para continuar >>')

os.system('cls' if os.name == 'nt' else 'clear')

opt = 0
while opt != 6:
    opt = int(input('\n\033[1mSelecione a opção desejada:\033[m\n[1] - Cadastrar novo voo\n[2] - Consultar voos\n[3] - Consultar passageiros de um voo\n[4] - Vender passsagens\n[5] - Cancelar passagens\n[6] - Sair\n>> '))

    if opt == 1:
        resposta = 'S'
        while resposta == 'S':
            num_voo = randint(1000, 9999)
            while num_voo in voos.keys():
                num_voo = randint(1000, 9999)
            informacoes.clear()
            informacoes.append(input('\nInforme a cidade de origem: ').upper())
            informacoes.append(input('Informe a cidade de destino: ').upper())
            informacoes.append(int(input('Informe a quantidade de escalas: ')))
            informacoes.append(float(input('Informe o valor das passagens: R$')))
            informacoes.append(int(input('Informe a quantidade de lugares disponíveis: ')))
            informacoes.append(list())
            voos[num_voo] = informacoes
            if voos[num_voo][4] > 0:
                voos_disponiveis.append(num_voo)
            print('\n\033[1m>> Voo cadastrado com sucesso! <<\033[m')
            resposta = input('Deseja continuar cadastrando? [S/N]\n>> ').upper()
            while resposta != 'S' and resposta != 'N':
                resposta = input('Resposta inválida. Digite "S" para SIM e "N" para NÃO.\n>> ').upper()

    elif opt == 2:
        opt = 0
        while opt not in [1, 2, 3, 4, 5]:
            opt = int(input('\n\033[1mSelecione a opção desejada:\033[m\n[1] - Buscar pelo código\n[2] - Buscar pela cidade de origem\n[3] - Buscar pela cidade de destino\n[4] - Buscar o voo com menor escala\n[5] - Listar todos\n>> '))

            if opt == 1:
                if voos != {}:
                    codigo_busca = int(input('\nInforme o código do voo para consulta: '))
                    if codigo_busca in voos.keys():
                        for voo in voos.items():
                            if voo[0] == codigo_busca:
                                print('-'*60)
                                exibe_dados_voo(voo)
                                print('-'*60)
                                break
                    else:
                        print(f'\n\033[1;31m{">> NENHUM VOO ENCONTRADO <<":^60}\033[m')
                else:
                    print(f'\n\033[1;31m{">> NENHUM VOO CADASTRADO <<":^60}\033[m')
                    
            elif opt == 2:
                if voos != {}:
                    cidade_origem = input('\nInforme a cidade de origem para consulta: ').upper()
                    achou = 0
                    print(f'\n{f">> VOOS CADASTRADOS COM SAÍDA DE {cidade_origem} <<":^60}')
                    print('-'*60)
                    for voo in voos.items():
                        if voo[1][0] == cidade_origem.upper():
                            exibe_dados_voo(voo)
                            print('-'*60)
                            achou = 1
                    if achou == 0:
                        print(f'\n\033[1;31m{">> NENHUM VOO ENCONTRADO <<":^60}\033[m')
                else:
                    print(f'\n\033[1;31m{">> NENHUM VOO CADASTRADO <<":^60}\033[m')

            elif opt == 3:
                if voos != {}:
                    cidade_destino = input('\nInforme a cidade de destino para consulta: ').upper()
                    achou = 0
                    print(f'\n{f">> VOOS CADASTRADOS COM DESTINO PARA {cidade_destino} <<":^60}')
                    print('-'*60)
                    for voo in voos.items():
                        if voo[1][1] == cidade_destino.upper():
                            exibe_dados_voo(voo)
                            print('-'*60)
                            achou = 1
                    if achou == 0:
                        print(f'\n\033[1;31m{">> NENHUM VOO ENCONTRADO <<":^60}\033[m')
                else:
                    print(f'\n\033[1;31m{">> NENHUM VOO CADASTRADO <<":^60}\033[m')

            elif opt == 4:
                if voos != {}:
                    cidade_origem = input('\nInforme a cidade de origem para consulta: ').upper()
                    cidade_destino = input('Informe a cidade de destino para consulta: ').upper()
                    cont = 0
                    achou = 0
                    for voo in voos.items():
                        if voo[1][0] == cidade_origem and voo[1][1] == cidade_destino:
                            achou = 1
                            if cont == 0:
                                menor = voo[1][2]
                            else:
                                if voo[1][2] < menor:
                                    menor = voo[1][2]
                            cont += 1
                    if achou == 1:
                        print(f'\n\033[1m{f">> VOOS COM MENOR ESCALA SAINDO DE {cidade_origem} COM DESTINO A {cidade_destino} <<":^60}\033[m')
                        print('-'*60)
                        for voo in voos.items():
                            if voo[1][2] == menor:
                                exibe_dados_voo(voo)
                                print('-'*60)
                    else:
                        print(f'\n\033[1;31m{">> NENHUM VOO ENCONTRADO <<":^60}\033[m')
                else:
                    print(f'\n\033[1;31m{">> NENHUM VOO CADASTRADO <<":^60}\033[m')

            elif opt == 5:
                if voos != {}:
                    print(f'\n{">> VOOS CADASTRADOS <<":^60}')
                    print('-'*60)
                    for voo in voos.items():
                        exibe_dados_voo(voo)
                        print('-'*60)
                else:
                    print(f'\n\033[1;31m{">> NENHUM VOO CADASTRADO <<":^60}\033[m')

            else:
                print('\033[1;31mOpção inválida. Tente novamente...\033[m')

    elif opt == 3:
        if voos != {} and passageiros != {}:
            if passagens == []:
                codigo_busca = int(input('\nInforme o código do voo para consultar os passageiros: '))
                achou = 0
                achou_passageiro = 0
                for voo in voos.items():
                    if voo[0] == codigo_busca:
                        print(f'\n\033[1mQuantidade de lugares disponíveis:\033[m {voo[1][4]}\n\033[1mPassageiros do voo: \033[m')
                        for passageiro in voo[1][5]:
                            print(f'- \033[1mNome:\033[m {passageiros[passageiro][0]}; \033[1mCPF:\033[m {passageiro}; \033[1mTelefone:\033[m {passageiros[passageiro][1]}')
                            achou_passageiro = 1
                        if achou_passageiro == 0:
                            print('Esse voo ainda não possui passageiros')
                        achou = 1
                        break
                if achou == 0:
                    print(f'\n\033[1;31m{">> NENHUM VOO ENCONTRADO <<":^60}\033[m')
            else:
                print(f'\n\033[1;31m{">> NENHUMA PASSAGEM FOI VENDIDA AINDA <<":^60}\033[m')
        else:
            print(f'\n\033[1;31m{">> NENHUM VOO OU PASSAGEIRO CADASTRADO <<":^60}\033[m')

    elif opt == 4:
        if voos != {}:
            resposta = 'S'
            while resposta == 'S':
                cpf = input('\nInforme o CPF do comprador da passagem seguindo o modelo XXX.XXX.XXX-XX: ')
                while cpf not in passageiros.keys():
                    resposta = input('O CPF digitado não consta nos registros.\nDeseja cadastrá-lo no sistema? [S/N]\n>> ').upper()
                    while resposta != 'S' and resposta != 'N':
                        resposta = input('Resposta inválida. Digite "S" para SIM e "N" para NÃO.\n>> ').upper()
                    if resposta == 'S':
                        print(f'\033[1m{">> CADASTRO DE PASSAGEIROS <<":^60}\033[m\n')
                        informacoes.clear()
                        informacoes.append(input('Informe o nome do novo passageiro: ').title())
                        informacoes.append(input('Informe o telefone do novo passageiro no modelo (XX)XXXXX-XXXX: '))
                        informacoes.append(list())
                        passageiros[cpf] = informacoes
                        print(f'\n\033[1m{">> CADASTRO CONCLUÍDO <<":^60}\033[m\n\nProsseguindo com a compra da passagem...\n')
                    else:
                        cpf = input('Informe o CPF do comprador da passagem seguindo o modelo XXX.XXX.XXX-XX: ')
                codigo_busca = int(input('Informe o código do voo para o qual deseja comprar a passagem: '))
                while codigo_busca not in voos.keys():
                    codigo_busca = int(input('O voo informado não consta nos registros. Informe novamente o código do voo para o qual deseja comprar a passagem: '))
                if codigo_busca in voos_disponiveis:
                    if cpf not in voos[codigo_busca][5]:
                        voos[codigo_busca][5].append(cpf)
                    passagens.append([codigo_busca,cpf])
                    voos[codigo_busca][4] -= 1
                    if voos[codigo_busca][2] == 0:
                        voos_disponiveis.remove(codigo_busca)
                    if codigo_busca not in passageiros[cpf][2]:
                        passageiros[cpf][2].append(codigo_busca)
                    print('\n\033[1m>> Venda concluída com sucesso! <<\033[m')
                else:
                    print('Esse voo está lotado! Não foi possível realizar a compra da passagem.')
                resposta = input('Deseja continuar comprando? [S/N]\n>> ').upper()
                while resposta != 'S' and resposta != 'N':
                    resposta = input('Resposta inválida. Digite "S" para SIM e "N" para NÃO.\n>> ').upper()
        else:
            print(f'\n\033[1;31m{">> NENHUM VOO CADASTRADO <<":^60}\033[m')

    elif opt == 5:
        if voos != {} and passageiros != {}:
            if passagens != []:
                resposta = 'S'
                while resposta == 'S':
                    cpf = input('\nInforme o CPF em que deseja cancelar a passagem seguindo o modelo XXX.XXX.XXX-XX: ')
                    while cpf not in passageiros.keys():
                        cpf = input('O CPF digitado não consta nos registros. Informe novamente o CPF em que deseja cancelar a passagem seguindo o modelo XXX.XXX.XXX-XX: ')
                    codigo_busca = int(input('Informe o código do voo para o qual deseja cancelar a passagem: '))
                    while codigo_busca not in voos.keys():
                        codigo_busca = int(input('O voo informado não consta nos registros. Informe novamente o código do voo para o qual deseja cancelar a passagem: '))
                    if [codigo_busca,cpf] in passagens:
                        qtde_passagens = passagens.count([codigo_busca, cpf])
                        if qtde_passagens <= 1:
                            voos[codigo_busca][5].remove(cpf)
                            passageiros[cpf][2].remove(codigo_busca)
                        passagens.remove([codigo_busca, cpf])
                        voos[codigo_busca][4] += 1
                        if codigo_busca not in voos_disponiveis and voos[codigo_busca][4] > 0:
                            voos_disponiveis.append(codigo_busca)
                        print('\n\033[1m>> Passagem cancelada com sucesso! <<\033[m')
                    else:
                        print('O passageiro indicado não faz parte desse voo! Não foi possível realizar o cancelamento da passagen.')
                    resposta = input('Deseja continuar cancelando? [S/N]\n>> ').upper()
                    while resposta != 'S' and resposta != 'N':
                        resposta = input('Resposta inválida. Digite "S" para SIM e "N" para NÃO.\n>> ').upper()
            else:
                print(f'\n\033[1;31m{">> NENHUMA PASSAGEM FOI VENDIDA AINDA <<":^60}\033[m')
        else:
            print(f'\n\033[1;31m{">> NENHUM VOO OU PASSAGEIRO CADASTRADO <<":^60}\033[m')

    elif opt == 6:
        print('\nEncerrando o programa...\n')
        break
    else:
        print('\033[1;31mOpção inválida. Tente novamente...\033[m')

print('-'*60)
print(f"\033[1m{'ATÉ LOGO...':^60}\033[m")
print('-'*60)