# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from send_email import *
import sys, argparse, time

parser = argparse.ArgumentParser(description="CSUFGCONFIRM")

group = parser.add_mutually_exclusive_group()

group.add_argument("-c",
                   "--cli",
                   action="store_true")

parser.add_argument('--email',
                    action = 'store',
                    dest = 'email',
                    required = True,
                    type=str,
                    help = 'E-mail para envio das notificações')

parser.add_argument('--senha',
                    action = 'store',
                    dest = 'senha',
                    required = True,
                    type=str,
                    help = 'Senha do email informado')

parser.add_argument('--chromedrivepath',
                    action = 'store',
                    dest = 'chromedrivepath',
                    required = False,
                    type=str,
                    help = 'Local do binário do Chromedrive')

args = parser.parse_args()

email = args.email
senha = args.senha
chromedrivepath = args.chromedrivepath

if args.cli:
    while True:
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--window-size=1420,1080')
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')

        browser = webdriver.Chrome(chrome_options=chrome_options)

        browser.get('https://centrodeselecao.ufg.br/fiscalizacao/sistema/confirmacao/1_confirmacao_chamada.php')
        # AUTENTICAÇÃO
        cpf = browser.find_element_by_id('cpf')
        cpf.send_keys('70182005127')
        acessar = browser.find_element_by_class_name('btn')
        acessar.click()

        # VISUALIZA CONCURSOS DISPONÍVEIS
        try:
            confirmar_interesse = browser.find_element_by_class_name('btn-primary')
            confirmar_interesse.click()
        except NoSuchElementException:
            print 'Não há concurso público disponível'
            enviar_email(email, senha, assunto="UFG - Nenhum concurso no momento", texto="")
        # TRATAMENTO DE CONCURSOS DISPONÍVEIS
        # enviar_email(email, senha, texto="Glória a deux", assunto="UFG - Novo concurso disponível!")
        time.sleep(30)
else:
    while True:
        browser = webdriver.Chrome()
        browser.get('https://centrodeselecao.ufg.br/fiscalizacao/sistema/confirmacao/1_confirmacao_chamada.php')

        #AUTENTICAÇÃO
        cpf = browser.find_element_by_id('cpf')
        cpf.send_keys('70182005127')
        acessar = browser.find_element_by_class_name('btn')
        acessar.click()

        #VISUALIZA CONCURSOS DISPONÍVEIS
        try:
            confirmar_interesse = browser.find_element_by_class_name('btn-primary')
            confirmar_interesse.click()
        except NoSuchElementException:
                print 'Não há concurso público disponível'
                enviar_email(email, senha, texto="Não existem concursos no momento.", assunto="UFG - Nenhum concurso no momento")

        #TRATAMENTO DE CONCURSOS DISPONÍVEIS
        #enviar_email(email, senha, texto="Glória a deux", assunto="UFG - Novo concurso disponível!")
        time.sleep(30)