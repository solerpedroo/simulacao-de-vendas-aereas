import os
from random import randint

voos = {1234: ['SP', 'BH', 2, 500.0, 107, ['123456789-00', '123456788-10', '147853698-11']], 1235: ['SP', 'BH', 0, 600.0, 120, []], 12366: ['SP', 'BH', 1, 550.0, 116, []]}
passageiros = {'123456789-00': ['Pessoa 1', '99999-1111', []], '123456788-10': ['Pessoa 2', '99999-1111', []], '147853698-11': ['Pessoa 3', '99999-1111', []]}
voos_disponiveis = []
informacoes = []

print('\n\n\t\033[1m=-=-=-=-= BEM VINDO(A) AO SISTEMA DE CONTROLE DE PASSAGENS AÉREAS =-=-=-=-=\033[m\n\n')
print('O sistema serve para cadastrar e consultar voos, consultar passsageiros e vender e cancelar passagens\n')
input('\n\t<< Tecle Enter para continuar >>')

os.system('cls' if os.name == 'nt' else 'clear')

opt = 0
while opt != 6:
    opt = int(input('\n\033[1mSelecione a opção desejada:\033[m\n[1] - Cadastrar novo voo\n[2] - Consultar voos\n[3] - Consultar passageiros de um voo\n[4] - Vender passsagens\n[5] - Cancelar passagens\n[6] - Sair\n>> '))

    if opt == 1:
        num_voo = randint(1000, 9999)
        while num_voo in voos.keys():
            num_voo = randint(1000, 9999)
        informacoes.clear()
        informacoes.append(input('\nInforme a cidade de origem: '))
        informacoes.append(input('Informe a cidade de destino: '))
        informacoes.append(int(input('Informe a quantidade de escalas: ')))
        informacoes.append(float(input('Informe o valor das passagens: R$')))
        informacoes.append(int(input('Informe a quantidade de lugares disponíveis: ')))
        informacoes.append(list())
        voos[num_voo] = informacoes
        print('\n\033[1m>> Voo cadastrado com sucesso! <<\033[m')
        
    elif opt == 2:
        opt = 0
        while opt not in [1, 2, 3, 4, 5]:
            opt = int(input('\n\033[1mSelecione a opção desejada:\033[m\n[1] - Buscar pelo código\n[2] - Buscar pela cidade de origem\n[3] - Buscar pela cidade de destino\n[4] - Buscar o voo com menor escala\n[5] - Listar todos\n>> '))

            if opt == 1:
                codigo_busca = int(input('\nInforme o código do voo para consulta: '))
                achou = 0
                for voo in voos.items():
                    if voo[0] == codigo_busca:
                        print(f'\n\033[1mCódigo:\033[m {voo[0]}\n\033[1mCidade de origem:\033[m {voo[1][0]}\n\033[1mCidade de destino:\033[m {voo[1][1]}\n\033[1mQuantidade de escalas:\033[m {voo[1][2]}\n\033[1mValor das passagens:\033[m R$ {voo[1][3]}\n\033[1mQuantidade de lugares disponíveis:\033[m {voo[1][4]}')
                        achou = 1
                        break
                if achou == 0:
                    print(f'\n\033[1;31m{">> Voo não encontrado <<":^60}\033[m')
                    
            elif opt == 2:
                cidade_origem = input('\nInforme a cidade de origem para consulta: ').upper()
                achou = 0
                print(f'\n{f">> VOOS CADASTRADOS COM SAÍDA DE {cidade_origem}<<":^60}')
                print('-'*60)
                for voo in voos.items():
                    if voo[1][0] == cidade_origem.upper():
                        print(f'\n\033[1mCódigo:\033[m {voo[0]}\n\033[1mCidade de origem:\033[m {voo[1][0]}\n\033[1mCidade de destino:\033[m {voo[1][1]}\n\033[1mQuantidade de escalas:\033[m {voo[1][2]}\n\033[1mValor das passagens:\033[m R$ {voo[1][3]}\n\033[1mQuantidade de lugares disponíveis:\033[m {voo[1][4]}\n')
                        print('-'*60)
                        achou = 1
                if achou == 0:
                    print(f'\n\033[1;31m{">> Voo não encontrado <<":^60}\033[m')

            elif opt == 3:
                cidade_destino = input('\nInforme a cidade de destino para consulta: ').upper()
                achou = 0
                print(f'\n{f">> VOOS CADASTRADOS COM DESTINO PARA {cidade_destino}<<":^60}')
                print('-'*60)
                for voo in voos.items():
                    if voo[1][1] == cidade_destino.upper():
                        print(f'\n\033[1mCódigo:\033[m {voo[0]}\n\033[1mCidade de origem:\033[m {voo[1][0]}\n\033[1mCidade de destino:\033[m {voo[1][1]}\n\033[1mQuantidade de escalas:\033[m {voo[1][2]}\n\033[1mValor das passagens:\033[m R$ {voo[1][3]}\n\033[1mQuantidade de lugares disponíveis:\033[m {voo[1][4]}\n')
                        print('-'*60)
                        achou = 1
                if achou == 0:
                    print(f'\n\033[1;31m{">> Voo não encontrado <<":^60}\033[m')

            elif opt == 4:
                cidade_origem = input('\nInforme a cidade de origem para consulta: ').upper()
                cidade_destino = input('Informe a cidade de destino para consulta: ').upper()
                cont = 0
                achou = 0
                for voo in voos.items():
                    if voo[1][0] == cidade_origem and voo[1][1] == cidade_destino:
                        achou = 1
                        if cont == 0:
                            menor = voo[1][2]
                            chave_menor = voo[0]
                        else:
                            if voo[1][2] < menor:
                                menor = voo[1][2]
                                chave_menor = voo[0]
                        cont += 1
                if achou == 1:
                    print(f'\n\033[1mVoo com menor escala: \nCódigo:\033[m {chave_menor}\n\033[1mCidade de origem:\033[m {voos[chave_menor][0]}\n\033[1mCidade de destino:\033[m {voos[chave_menor][1]}\n\033[1mQuantidade de escalas:\033[m {voos[chave_menor][2]}\n\033[1mValor das passagens:\033[m R$ {voos[chave_menor][3]}\n\033[1mQuantidade de lugares disponíveis:\033[m {voos[chave_menor][4]}\n')
                else:
                    print(f'\n\033[1;31m{">> Voo não encontrado <<":^60}\033[m')

            elif opt == 5:
                print(f'\n{">> VOOS CADASTRADOS <<":^60}')
                print('-'*60)
                for voo in voos.items():
                    print(f'\033[1mCódigo:\033[m {voo[0]}\n\033[1mCidade de origem:\033[m {voo[1][0]}\n\033[1mCidade de destino:\033[m {voo[1][1]}\n\033[1mQuantidade de escalas:\033[m {voo[1][2]}\n\033[1mValor das passagens:\033[m R$ {voo[1][3]}\n\033[1mQuantidade de lugares disponíveis:\033[m {voo[1][4]}')
                    print('-'*60)

            else:
                print('\033[1;31mOpção inválida. Tente novamente...\033[m')

    elif opt == 3:
        codigo_busca = int(input('\nInforme o código do voo para consultar os passageiros: '))
        achou = 0
        achou_passageiro = 0
        for voo in voos.items():
            if voo[0] == codigo_busca:
                print(f'\n\033[1mQuantidade de lugares disponíveis:\033[m {voo[1][4]}\n\033[1mPassageiros do voo: \033[m')
                for passageiro in voo[1][5]:
                    print(f'- \033[1mNome:\033[m {passageiros[passageiro][0]}; \033[1mCPF:\033[m {passageiro}')
                    achou_passageiro = 1
                if achou_passageiro == 0:
                    print('Esse voo ainda não possui passageiros')
                achou = 1
                break
        if achou == 0:
            print(f'\n\033[1;31m{">> Voo não encontrado <<":^60}\033[m')

    elif opt == 4:
        cpf = input('\nInforme o CPF do comprador da passagem: ')
        while cpf not in passageiros.keys():
            cpf = input('O CPF digitado não consta nos registros. Informe novamente o CPF do comprador da passagem: ')
        codigo_busca = int(input('Informe o código do voo para o qual deseja comprar a passagem: '))
        while codigo_busca not in voos.keys():
            codigo_busca = int(input('O voo informado não consta nos registros. Informe novamente o código do voo para o qual deseja comprar a passagem: '))
        if voos[codigo_busca][4] > 0:
            voos[codigo_busca][5].append(cpf)
            voos[codigo_busca][4] -= 1
            passageiros[cpf][2].append(codigo_busca)
            print('\n\033[1m>> Venda concluída com sucesso! <<\033[m')
        else:
            print('Esse voo está lotado! Não foi possível realizar a compra da passagem.')

    elif opt == 5:
        cpf = input('\nInforme o CPF em que deseja cancelar a passagem: ')
        while cpf not in passageiros.keys():
            cpf = input('O CPF digitado não consta nos registros. Informe novamente o CPF em que deseja cancelar a passagem: ')
        codigo_busca = int(input('Informe o código do voo para o qual deseja cancelar a passagem: '))
        while codigo_busca not in voos.keys():
            codigo_busca = int(input('O voo informado não consta nos registros. Informe novamente o código do voo para o qual deseja cancelar a passagem: '))
        if cpf in voos[codigo_busca][5]:
            voos[codigo_busca][5].remove(cpf)
            voos[codigo_busca][4] += 1
            passageiros[cpf][2].remove(codigo_busca)
            print('\n\033[1m>> Passagem cancelada com sucesso! <<\033[m')
        else:
            print('O passageiro indicado não faz parte desse voo! Não foi possível realizar o cancelamento da passagen.')
    elif opt == 6:
        print('\nEncerrando o programa...\n')
        break
    else:
        print('\033[1;31mOpção inválida. Tente novamente...\033[m')

print('-'*60)
print(f"\033[1m{'ATÉ LOGO...':^60}\033[m")
print('-'*60)