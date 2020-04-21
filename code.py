dicionario_pacientes = {}
dicionario_medicos = {}
dicionario_consultas = {}


def pacientes():
    nome_paciente = input('Insira o nome do paciente:').lower()
    dici = {
        'Email do paciente': input('Insira o email:'),
        'Telefone do paciente': input('Insira o telefone:'),
        'RG do paciente': input('Insira o RG:'),
        'CPF do paciente': input('Insira o CPF:'),
        'Endereço do paciente': input('Insira o endereço:'),
        'Número do paciente': input('Insira o número da residência:'),
        'Bairro do paciente': input('Insira o bairro:'),
        'Cidade do paciente': input('Insira a cidade:'),
        'UF do paciente': input('Insira o estado:'),
        'Plano do paciente': input('Insira o plano de saúde:'),

    }
    dicionario_pacientes[nome_paciente] = dici
    print('-' * 50)
    print('1-Voltar ao menu', '2-Encerrar programa')
    print('-' * 50)
    decisao = int(input('O que você deseja? :'))
    if decisao == 1:
        menu()
    else:
        print('Sistema de clínicas fechado com sucesso!')


def medicos():
    nome_medico = input('Insira o nome do médico:').lower()
    dici = {
        'Email do médico': input('Insira o email:'),
        'Telefone do médico': input('Insira o telefone:'),
        'RG do médico': input('Insira o RG:'),
        'CPF do médico': input('Insira o CPF:'),
        'Endereço do médico': input('Insira o endereço:'),
        'Número do médico': input('Insira o número da residência:'),
        'Bairro do médico': input('Insira o bairro:'),
        'Cidade do médico': input('Insira a cidade:'),
        'UF do médico': input('Insira o estado:'),
        'Plano do médico': input('Insira o plano de saúde:'),
        'CRM do médico': input('Insira o CRM:'),
        'Celular do médico': input('Insira o celular do médico'),
        'Especialização do médico': input('Insira a especialização:'),

    }
    dicionario_medicos[nome_medico] = dici
    print('-' * 50)
    print('1-Voltar ao menu', '2-Encerrar programa')
    print('-' * 50)
    decisao = int(input('O que você deseja? :'))
    if decisao == 1:
        menu()
    else:
        print('Sistema de clínicas fechado com sucesso!')


def consultas():
    paciente = input('Qual o seu nome?  :').lower()
    dici = {
        'Médico': input('Com qual médico será consultado?  :'),
        'Data': input('Qual a data da consulta?  :'),
        'Hora': input('Qual a hora da consulta?  :'),
    }
    dicionario_consultas[paciente] = dici
    print('-'*50)
    print('1-Voltar ao menu', '2-Encerrar programa')
    print('-' * 50)
    decisao = int(input('O que você deseja? :'))
    if decisao == 1:
        menu()
    else:
        print('Sistema de clínicas fechado com sucesso!')


def menu():
    print('-'*50)
    print('     O QUE VOCÊ GOSTARIA DE FAZER?      ')
    print("""
    1-Cadastrar paciente  5-Listar médicos
    2-Cadastrar médico    6-Listar consultas
    3-Marcar consulta     7-Remover médico
    4-Listar pacientes    8-Remover consulta
    9-Fechar programa
    """)
    print('-'*50)
    select = int(input('Digite aqui sua operação: '))
    if select == 1:
        pacientes()
    if select == 2:
        medicos()
    if select == 3:
        consultas()
    if select == 4:
        for chave in dicionario_pacientes.keys():
            print(chave)
        print('-' * 50)
        print('1-Voltar ao menu', '2-Encerrar programa')
        print('-' * 50)
        decisao = int(input('O que você deseja? :'))
        if decisao == 1:
            menu()
        else:
            print('Sistema de clínicas fechado com sucesso!')
    if select == 5:
        for chave in dicionario_medicos.keys():
            print(chave)
        print('-' * 50)
        print('1-Voltar ao menu', '2-Encerrar programa')
        print('-' * 50)
        decisao = int(input('O que você deseja? :'))
        if decisao == 1:
            menu()
        else:
            print('Sistema de clínicas fechado com sucesso!')
    if select == 6:
        for chave in dicionario_consultas.keys():
            print(chave)
        print('-' * 50)
        print('1-Voltar ao menu', '2-Encerrar programa')
        print('-' * 50)
        decisao = int(input('O que você deseja? :'))
        if decisao == 1:
            menu()
        else:
            print('Sistema de clínicas fechado com sucesso!')
    if select == 7:
        del dicionario_medicos[input('Digite o nome do médico a ser removido:').lower()]
        print('-' * 50)
        print('1-Voltar ao menu', '2-Encerrar programa')
        print('-' * 50)
        decisao = int(input('O que você deseja? :'))
        if decisao == 1:
            menu()
        else:
            print('Sistema de clínicas fechado com sucesso!')
    if select == 8:
        del dicionario_consultas[input('Digite o nome do paciente que marcou a consulta:').lower()]
        print('-' * 50)
        print('1-Voltar ao menu', '2-Encerrar programa')
        print('-' * 50)
        decisao = int(input('O que você deseja? :'))
        if decisao == 1:
            menu()
        else:
            print('Sistema de clínicas fechado com sucesso!')
    if select == 9:
        print('Sistemas de clínicas fechado com sucesso!')
    if select > 9 or select < 1:
        print('Sua operação não existe!')


menu()
