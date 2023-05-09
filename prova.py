# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 20:43:17 2023

@author: wellynton
"""
from datetime import datetime
from dateutil import relativedelta

def informar_float(mensagem):
    try:
        valor = float(input(mensagem))
        return valor;
    except ValueError:
        print('inválido!') 
        return informar_float(mensagem)

def informar_inteiro(mensagem):
    try:
        valor = int(input(mensagem))
        return valor;
    except ValueError:
        print('inválido!') 
        return informar_inteiro(mensagem)

def retornar_saldo(ano, mes):
    with open('salario.txt', 'r') as arquivo:
        linhas = arquivo.readlines();
        for linha in linhas:
            registro = linha.split(',')
            if (ano == int(registro[0]) and mes == int(registro[1])):
                return registro[2]

def buscar_total_despesa(ano, mes):
    with open('despesa.txt', 'r') as arquivo:
        linhas = arquivo.readlines();
        total = 0
        for linha in linhas:
            registro = linha.split(',')
            if (int(ano) == int(registro[0]) and int(mes) == int(registro[1])):
                total = registro[2]
            
        return total

def calcular_rendimento(valor, ano, mes):
    d1 = '01/' + mes + '/'+ ano
    d2 = '01/'+ str(datetime.now().month)+'/' + str(datetime.now().year)
    
    start_date = datetime.strptime(d1, "%d/%m/%Y")
    end_date = datetime.strptime(d2, "%d/%m/%Y")
    
    delta = relativedelta.relativedelta(end_date, start_date)
    total_meses = delta.months + (delta.years * 12)    
    taxa = 0.01
    return valor * (1 + taxa) ** total_meses

menu = input("Informe a opção desejada: (1 - Informar salário 2 - Alterar salário) ")

if (menu == '1'):
    with open('salario.txt', 'a+') as arquivo:
        ano = informar_inteiro('Informe o ano: ')
        mes =  informar_inteiro('Informe o mês: ')
        salario = informar_float('Informe o salário: ')
        
        linha = str(ano) + ',' + str(mes) + ',' + str(salario)
        arquivo.write(linha)
        arquivo.write('\n')
        
elif (menu == '2'):
    ano = informar_inteiro('Informe o ano: ')
    mes =  informar_inteiro('Informe o mês: ')
    salario = informar_float('Informe o novo salário: ')
    linha_alterada = 0
    linhas = []
    with open('salario.txt', 'r') as arquivo:
        linhas = arquivo.readlines();
        for linha in linhas:
            registro = linha.split(',')
            if (ano == int(registro[0]) and mes == int(registro[1])):
                linha_alterada = linhas.index(linha)          
        
        linhas[linha_alterada] = str(ano) + ',' + str(mes) + ',' + str(salario) + '\n'
        
    with open('salario.txt', 'w') as arquivo:
        arquivo.writelines(linhas)
elif (menu == '3'):
    ano = informar_inteiro('Informe o ano: ')
    mes =  informar_inteiro('Informe o mês: ')
    linha_alterada = 0
    linhas = []
    with open('salario.txt', 'r') as arquivo:
        linhas = arquivo.readlines();
        for linha in linhas:
            registro = linha.split(',')
            if (ano == int(registro[0]) and mes == int(registro[1])):
                linha_alterada = linhas.index(linha)  
    
    linhas.pop(linha_alterada)
    with open('salario.txt', 'w') as arquivo:
        arquivo.writelines(linhas)
elif (menu == '4'):
    with open('salario.txt', 'r') as arquivo:
        linhas = arquivo.readlines();
        linhas.sort()
        print(linhas)
        print('----Salários----')
        for linha in linhas:
            registro = linha.split(',')
            print('Ano: ' + registro[0] + ' Mês: ' + registro[1] + ' Salário: ' + registro[2])

elif (menu == '5'):
    ano = informar_inteiro('Informe o ano: ')
    mes =  informar_inteiro('Informe o mês: ')
    despesa = informar_float('Informe a despesa: ')
    
    saldo_mes = float(retornar_saldo(ano, mes))
    
    if despesa > saldo_mes:
        print('Saldo insuficiente!')
    else:   
        with open('despesa.txt', 'a+') as arquivo:
            linha = str(ano) + ',' + str(mes) + ',' + str(despesa) + ';'
            arquivo.write(linha)
            arquivo.write('\n')
elif (menu == '9'):
    with open('salario.txt', 'r') as arquivo:
        linhas = arquivo.readlines();
        linhas.sort()
        print(linhas)
        print('----Salários----')
        for linha in linhas:
            registro = linha.split(',')
            print('Ano: ' + registro[0] + ' Mês: ' + registro[1])
            salario = float(registro[2]);
            print('Salário: ' + str(salario))
            total_despesa = buscar_total_despesa(registro[0], registro[1])
            print('Despesa: ', total_despesa)
            saldo = salario - float(total_despesa)
            print('Saldo: ', saldo)
            bateu_meta = saldo > (salario * 0.1)
            print('Meta: ', bateu_meta)
            print('Valor investido: ', saldo)
            rendimento = calcular_rendimento(saldo, registro[0], registro[1])
            print('Rendimento: ', rendimento)


