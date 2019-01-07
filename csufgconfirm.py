# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from send_email import *
import argparse, time

parser = argparse.ArgumentParser(description="CSUFGCONFIRM")
group = parser.add_mutually_exclusive_group()
url = 'https://centrodeselecao.ufg.br/fiscalizacao/sistema/confirmacao/1_confirmacao_chamada.php'
url_teste='C:\Users\João Paulo\Desktop\Centro de Seleção UFG - Fiscalização.html'

group.add_argument("--cli",
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

parser.add_argument('--cdpath',
                    action = 'store',
                    dest = 'chromedriverpath',
                    required = True,
                    type=str,
                    help = 'Local do binário do Chromedriver')

parser.add_argument('--cpf',
                    action = 'store',
                    dest = 'cpf',
                    required = True,
                    type=str,
                    help = 'CPF do Usuário')

args = parser.parse_args()

email = args.email
senha = args.senha
chromedriverpath = args.chromedriverpath
login = args.cpf


if args.cli:
    while True:
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--window-size=1420,1080')
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')

        browser = webdriver.Chrome(chromedriverpath,chrome_options=chrome_options)

        browser.get(url)
        # AUTENTICAÇÃO
        cpf = browser.find_element_by_id('cpf')
        cpf.send_keys(login)
        acessar = browser.find_element_by_class_name('btn')
        acessar.click()

        # VISUALIZA CONCURSOS DISPONÍVEIS
        try:
            confirmar_interesse = browser.find_element_by_class_name('btn-primary')
            confirmar_interesse.click()

            # TRATAMENTO DE CONCURSOS DISPONÍVEIS
            print 'Há concursos públicos disponíveis'
            enviar_email(email, senha, texto="Mais informações em "+url, assunto="UFG - Novo concurso disponível!")
        except NoSuchElementException:
            print 'Não há concurso público disponível'

        time.sleep(30)
else:
    while True:
        browser = webdriver.Chrome(chromedriverpath)
        browser.get(url)

        #AUTENTICAÇÃO
        cpf = browser.find_element_by_id('cpf')
        cpf.send_keys(login)
        acessar = browser.find_element_by_class_name('btn')
        acessar.click()

        #VISUALIZA CONCURSOS DISPONÍVEIS
        try:
            confirmar_interesse = browser.find_element_by_class_name('btn-primary')
            confirmar_interesse.click()

            # TRATAMENTO DE CONCURSOS DISPONÍVEIS
            print 'Há um concurso público disponível'
            enviar_email(email, senha, texto="Mais informações em " + url, assunto="UFG - Novo concurso disponível!")
        except NoSuchElementException:
                print 'Não há concurso público disponível'

        time.sleep(30)
