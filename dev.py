#!/usr/bin/env python
# coding: utf-8

# In[147]:


# O usuario entra no portal e se depara com uma tela onde ele pode:
# Login / Cadastro / 'Esqueci minha senha' 


# In[148]:


def validar_cpf_2(cpf):
    
    corpo_cpf = cpf[:9]
    digito_cpf = cpf[-2:]

    calculo_1 = 0
    calculo_2 = 0
    
    multiplicacao = [10, 9, 8, 7, 6, 5, 4, 3, 2]
    
    for i, j in zip(multiplicacao, corpo_cpf):
        calculo_1 += i * int(j)
    #print(f'Cálculo 1: {calculo_1}')
    
    resto_1 = calculo_1 % 11
    #print(f'Resto 1: {resto_1}')
    
    digito_1 = 0 if resto_1 < 2 else 11 - resto_1
    #print(f'Dígito 1: {digito_1}\n')
    
    corpo_cpf += str(digito_1)
    
    for i, j in zip(multiplicacao, corpo_cpf[1:]):
        calculo_2 += i * int(j)
    
    #print(f'Cálculo 2: {calculo_2}')
    
    resto_2 = calculo_2 % 11
    #print(f'Resto 2: {resto_2}')
    
    digito_2 = 0 if resto_2 < 2 else 11 - resto_2
    #print(f'Dígito 2: {digito_2}')
    
    return digito_cpf == f'{digito_1}{digito_2}'


# In[149]:


# cadastro
# Iremos cadastrar os pacientes com base em seu CPF pois pensamos em atender tanto planos de saude, quanto SUS
    
def valida_cpf():

    blocklist = [
        '00000000000',
        '11111111111',
        '22222222222',
        '33333333333',
        '44444444444',
        '55555555555',
        '66666666666',
        '77777777777',
        '88888888888',
        '99999999999'
    ]

    while True:  
        nome = input(str('Digite seu nome: '))
        entrada = input(str('Digite seu CPF: '))
        entrada_sem_ponto = entrada.replace('.', '')
        entrada = entrada_sem_ponto.replace('-', '')

        arquivo = open('registrados.txt', 'r')
        arquivo.readlines()
        
        print(arquivo.readlines())
        
        if entrada in arquivo:
            print('Usuario ja cadastrado')
        
        if entrada.isnumeric():

            if len(entrada) == 11:

                if entrada in blocklist:

                    print('> O CPF não pode ter todos os números iguais!\n')

                else:

                    if validar_cpf_2(entrada):
                        print('# CPF Válido!\n')
                        break

                    else:
                        print('# CPF Inválido!\n')
            else:

                print('> O número de CPF deve ter 11 dígitos!\n')

    dt_ncsto = input(str('Digite sua data de nascimento (ex: ddmmaa (010203)): '))


# In[150]:


def cadastrar(): 
    print('Olá, vamos criar as credenciais de sua nova conta!')
    
    entrada = str(valida_cpf())
    senha = input(str('Defina sua senha: '))
    
    # validar senha
    valida_senha = input(str('Repita sua senha: '))

    if senha != valida_senha:

            print('As senhas nao coincidem!')
            definicao_senha()
    else:
            print(valida_senha)
            print('Senha valida!')
            
    cadastro = str(entrada + senha)
    
    check = str(entrada + senha)
    
    with open('/Users/daniel.magalhaes/Documents/logins/registros.txt', 'r') as arquivo:
        while not cadastro in check:
            with open('/Users/daniel.magalhaes/Documents/logins/registros.txt', 'w') as arquivo:
                arquivo.write(str(cadastro))
                print('Armazenado com sucesso')
        while cadastro in check:
            print('faça login!')
            break


# In[151]:


# login
# Para o login será considerado: CPF e Senha definida no cadastro
# Valida o login com a base gerada via vetor no cadastro 

def login():
    login = input(str('Digite seu login (Seu CPF): '))
    senha = input(str('Digite sua senha: '))
    
    login = login + senha
    
    with open('/Users/daniel.magalhaes/Documents/logins/registros.txt', 'r') as arquivo: 
        check = arquivo.readlines()
        while not login in check:
            print('login nao encontrado!')
            break
        while login in check:
            print('login efetuado com sucesso')
            break


# In[152]:


def login_medico():
    login = input(str('Digite seu login (Seu CRM): '))
    senha = input(str('Digite sua senha: '))
    
    login = login + senha
    
    with open('/Users/daniel.magalhaes/Documents/crms/registros.txt', 'r') as arquivo: 
        check = arquivo.readlines()
        while not login in check:
            print('login nao encontrado!')
            break
        while login in check:
            print('login efetuado com sucesso')
            break


# In[153]:


def cadastrar_medico(): 
    print('Olá, vamos criar as credenciais de sua nova conta!')
    
    entrada = input(str('Digite seu CRM: '))
    if len(entrada) != 5:
        print('CRM Incorreto!')
        entrada = input(str('Digite seu CRM: '))
    while len(entrada) == 5:
        print('CRM Correto!')
        break
        
    senha = input(str('Defina sua senha: '))
    
    # validar senha
    valida_senha = input(str('Repita sua senha: '))

    if senha != valida_senha:

            print('As senhas nao coincidem!')
            definicao_senha()
    else:
            print(valida_senha)
            print('Senha valida!')
            
    cadastro = entrada + senha
    
    check = entrada + senha
    
    with open('/Users/daniel.magalhaes/Documents/crms/registros.txt', 'r') as arquivo:
        while not cadastro in check:
                with open('/Users/daniel.magalhaes/Documents/crms/registros.txt', 'w') as arquivo:
                    arquivo.write(cadastro)
                    print('Armazenado com sucesso')
        while cadastro in check:
            print('faça login!')
            break


# In[154]:


# esqueci minha senha
# Por nao termos integracao com banco de dados, neste momento jogaremos o usuario para a etapa de cadastro
def redefinicao_senha(): 
    pessoa = input(str('''Voce é:
                       1 - Medico 
                       2 - Paciente ou atendente
                       '''))
    if pessoa == '1':
        print('Refaca seu cadastro')
        cadastro_medico()
    elif pessoa == '2': 
        print('Refaca seu cadastro')
        cadastro()


# In[155]:


def registrar_relatorio():
     
    nome = input(str('Nome do paciente: '))
    cpf = input(str('CPF do paciente: '))
    while len(cpf) < 11: 
        print('O CPF do paciente deve conter 11 digitos')
        cpf = str(input('CPF do paciente: '))
    pal_chave = input('Digite as palavras referencias do atendimento: ')
    prontuario = input(str('Digite o que foi identificado no atendimento: '))
    receita = input(str('Digite o que foi receitado: '))
    print('Relatorio gerado com sucesso!')
    
    relatorio = [
     nome,
     pal_chave,
     prontuario,
     receita 
    ]
    
    with open('/Users/daniel.magalhaes/Documents/Relatorios/' + cpf + '.txt', 'w') as arquivo: 
        arquivo.write(str(relatorio))
        
    # somente o medico tera acesso a essa funcao


# In[156]:


def consultar_relatorio():
    
    arquivo = input(str('Digite o nome do arquivo que deseja abrir: '))
    
    with open('/Users/daniel.magalhaes/Documents/Relatorios/' + arquivo + '.txt', 'r') as arquivo: 
        arquivo = arquivo.read()
        print(arquivo)
    
    # todas entidades acessam essa funcao 


# In[157]:


# Execucao do programa 
def execucao():
    print(' --- Seja bem vindo ao Health BR ---')
    print(' - Developed by: Green Code -')
    pessoa = input(str('''
    Digite sua identificacao: 
    1 - Medico
    2 - Paciente ou atendente
    '''))
    if pessoa == '1': 
        print(' --------------- Menu --------------')
        print('''
        1 - Login
        2 - Cadastro
        3 - Esqueci minha senha''')
        print(' -----------------------------------')
        n = input(str('Digite o que deseja acessar: '))
        if n == '1':
            login_medico()
            sistema_medico()
        elif n == '2':
            cadastrar_medico()
            print('Faca seu login!')
            execucao()
        elif n == '3':
            redefinicao_senha()
        else:
                print('O valor digitado nao está no menu de opcoes')

    elif pessoa == '2':
        print(' --------------- Menu --------------')
        print('''
        1 - Login
        2 - Cadastro
        3 - Esqueci minha senha''')
        print(' -----------------------------------')
        n = input(str('Digite o que deseja acessar: '))
        if n == '1':
            login()
            sistema()
        elif n == '2':
            cadastrar()
            print('Faca seu login!')
            execucao()
        elif n == '3':
            redefinicao_senha()
        else:
                print('O valor digitado nao está no menu de opcoes')


# In[158]:


def sistema_medico():
    print(' --- Seja bem vindo ao Health BR ---')
    print(' - Developed by: Green Code -')
    print(' --------------- Menu --------------')
    print('''1 - Registrar relatorio
    2 - Consultar relatorio
    3 - Sair
    ''')
    print(' -----------------------------------')
    n = input(str('Digite o que deseja acessar: '))
    if n == '1': 
        print('Vamos lá!')
        registrar_relatorio()
    elif n == '2':
        print('Vamos lá!')
        consultar_relatorio()
    elif n == '3':
        print('até logo!')
        execucao()


# In[159]:


def sistema():
    print(' --- Seja bem vindo ao Health BR ---')
    print(' - Developed by: Green Code -')
    print(' --------------- Menu --------------')
    print('''1 - Consultar relatorio
    2 - Sair
    ''')
    print(' -----------------------------------')
    n = input(str('Digite o que deseja acessar: '))
    if n == '1': 
        print('Vamos lá!')
        consultar_relatorio()
    elif n == '2':
        print('até logo!')
        execucao()


# In[163]:


execucao()

