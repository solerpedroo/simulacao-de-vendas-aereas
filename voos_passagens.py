import os
from random import randint

voos = {1234: ['SP', 'BH', 2, 500.0, 80, ['123456789-00', '123456788-10', '147853698-11']], 1235: ['SP', 'BH', 0, 600.0, 80, []], 12366: ['SP', 'BH', 1, 550.0, 80, []]}
passageiros = {'123456789-00': ['Pessoa 1', '99999-1111', []], '123456788-10': ['Pessoa 2', '99999-1111', []], '147853698-11': ['Pessoa 3', '99999-1111', []]}
voos_disponiveis = []
informacoes = []

print('\n\n\t\033[1m=-=-=-=-= BEM VINDO(A) AO SISTEMA PARA CONTROLE DE PASSAGENS AÉREAS =-=-=-=-=\033[m\n\n')
print('O sistema serve para você cadastrar e consultar voos, consultar passsageiros, vender e cancelar passagens\n')
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
        informacoes.append(input('Informe a cidade de origem: '))
        informacoes.append(input('Informe a cidade de destino: '))
        informacoes.append(int(input('Informe a quantidade de escalas: ')))
        informacoes.append(float(input('Informe o valor das passagens: ')))
        informacoes.append(int(input('Informe a quantidade de lugares disponíveis: ')))
        informacoes.append(list())
        voos[num_voo] = informacoes
        
    elif opt == 2:
        opt = 0
        while opt not in [1, 2, 3, 4]:
            opt = int(input('\n\033[1mSelecione a opção desejada:\033[m\n[1] - Buscar pelo código\n[2] - Buscar pela cidade de origem\n[3] - Buscar pela cidade de destino\n[4] - Buscar o voo com menor escala\n>> '))
            if opt == 1:
                codigo_busca = int(input('Informe o código do voo para consulta: '))
                achou = 0
                for voo in voos.items():
                    if voo[0] == codigo_busca:
                        print(f'\n\033[1mCódigo:\033[m {voo[0]}\n\033[1mCidade de origem:\033[m {voo[1][0]}\n\033[1mCidade de destino:\033[m {voo[1][1]}\n\033[1mQuantidade de escalas:\033[m {voo[1][2]}\n\033[1mValor das passagens:\033[m R$ {voo[1][3]}\n\033[1mQuantidade de lugares disponíveis:\033[m {voo[1][4]}')
                        achou = 1
                        break
                if achou == 0:
                    print('\n\033[1mVoo não encontrado\033[m')
                    
            elif opt == 2:
                cidade_origem = input('Informe a cidade de origem para consulta: ').upper()
                achou = 0
                for voo in voos.items():
                    if voo[1][0] == cidade_origem.upper():
                        print(f'\n\033[1mCódigo:\033[m {voo[0]}\n\033[1mCidade de origem:\033[m {voo[1][0]}\n\033[1mCidade de destino:\033[m {voo[1][1]}\n\033[1mQuantidade de escalas:\033[m {voo[1][2]}\n\033[1mValor das passagens:\033[m R$ {voo[1][3]}\n\033[1mQuantidade de lugares disponíveis:\033[m {voo[1][4]}\n')
                        achou = 1
                if achou == 0:
                    print('\n\033[1mVoo não encontrado\033[m')

            elif opt == 3:
                cidade_destino = input('Informe a cidade de destino para consulta: ').upper()
                achou = 0
                for voo in voos.items():
                    if voo[1][1] == cidade_destino.upper():
                        print(f'\n\033[1mCódigo:\033[m {voo[0]}\n\033[1mCidade de origem:\033[m {voo[1][0]}\n\033[1mCidade de destino:\033[m {voo[1][1]}\n\033[1mQuantidade de escalas:\033[m {voo[1][2]}\n\033[1mValor das passagens:\033[m R$ {voo[1][3]}\n\033[1mQuantidade de lugares disponíveis:\033[m {voo[1][4]}\n')
                        achou = 1
                if achou == 0:
                    print('\n\033[1mVoo não encontrado\033[m')

            elif opt == 4:
                cidade_origem = input('Informe a cidade de origem para consulta: ').upper()
                cidade_destino = input('Informe a cidade de destino para consulta: ').upper()
                cont = 0
                for voo in voos.items():
                    if voo[1][0] == cidade_origem and voo[1][1] == cidade_destino:
                        if cont == 0:
                            menor = voo[1][2]
                            chave_menor = voo[0]
                        else:
                            if voo[1][2] < menor:
                                menor = voo[1][2]
                                chave_menor = voo[0]
                        cont += 1

                print(f'\n\033[1mVoo com menor escala: \nCódigo:\033[m {chave_menor}\n\033[1mCidade de origem:\033[m {voos[chave_menor][0]}\n\033[1mCidade de destino:\033[m {voos[chave_menor][1]}\n\033[1mQuantidade de escalas:\033[m {voos[chave_menor][2]}\n\033[1mValor das passagens:\033[m R$ {voos[chave_menor][3]}\n\033[1mQuantidade de lugares disponíveis:\033[m {voos[chave_menor][4]}\n')
                
            else:
                print('\033[1;31mOpção inválida. Tente novamente...\033[m')
    elif opt == 3:
        codigo_busca = int(input('Informe o código do voo para consultar os passageiros: '))
        achou = 0
        for voo in voos.items():
            if voo[0] == codigo_busca:
                print(f'\n\033[1mQuantidade de lugares disponíveis:\033[m {voo[1][4]}\n\033[1mPassageiros do voo: \033[m')
                for passageiro in voo[1][5]:
                    print(f'- Nome: {passageiros[passageiro][0]}; CPF: {passageiro}')
                achou = 1
                break
        if achou == 0:
            print('\n\033[1mVoo não encontrado\033[m')
    elif opt == 4:
        codigo_busca = int(input('Informe o código do voo que deseja comprar: '))
        cpf = input('Informe o CPF em que deseja comprar a passagem: ')
        if voos[codigo_busca][4] > 0:
            voos[codigo_busca][5].append(cpf)
            voos[codigo_busca][4] -= 1
            passageiros[cpf][2].append(codigo_busca)
            print('>> Venda concluída com sucesso! <<')
    elif opt == 5:
        print('Cancelou')
    elif opt == 6:
        print('\nEncerrando o programa...\n')
        break
    else:
        print('\033[1;31mOpção inválida. Tente novamente...\033[m')

print('Adeus')