# -*- coding: utf-8 -*-
import argparse, selenium
from csufgconfirm import iniciar
from persistencia import *

parser = argparse.ArgumentParser(description="CSUFGCONFIRM")
group = parser.add_mutually_exclusive_group()

group.add_argument("--cli",
                   action="store_true")

args = parser.parse_args()

if args.cli is True and primeiraVez() is False:
    modo = 'cli'
    try:
        iniciar(getCpf(),getEmail(),getSenha(),getCdpath(),'CLI')
    except selenium.common.exceptions.WebDriverException:
        print "O ChromeDriver não foi encontrado no diretório informado."


elif primeiraVez() is True:
    print 'Bem vindo ao CSUFGCONFIRM!'
    print 'Por favor informe os dados para que possamos monitorar para você.'
    cpf = raw_input('Insira o CPF: ')
    email = raw_input('Insira o Email: ')
    senha = raw_input('Insira a senha do Email: ')
    cdpath = raw_input('Insira o local de instalação ChromeDriver: ')
    salvar_dados(cpf,email,senha,cdpath)

    trava = True
    while trava is True:
        print 'Modo Visual(GUI) ou Linha de Comando(CLI)?'
        modo = raw_input('Informe GUI ou CLI: ')
        if modo is 'CLI' or modo is'cli' or modo is 'GUI' or modo is 'gui':
            trava = False
    try:
        iniciar(getCpf(),getEmail(),getSenha(),getCdpath(),modo)
    except selenium.common.exceptions.WebDriverException:
        print "O ChromeDriver não foi encontrado no diretório informado."

elif primeiraVez() is False and args.cli is False:
    try:
        iniciar(getCpf(),getEmail(),getSenha(),getCdpath(),'GUI')
    except selenium.common.exceptions.WebDriverException:
        print "O ChromeDriver não foi encontrado no diretório informado."

