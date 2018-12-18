# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from send_email import *
import sys
import argparse

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

args = parser.parse_args()

email = args.email
senha = args.senha

if args.cli:
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--window-size=1420,1080')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')

    browser = webdriver.Chrome(chrome_options=chrome_options)

    browser.get('https://centrodeselecao.ufg.br/fiscalizacao/sistema/confirmacao/1_confirmacao_chamada.php')
else:
    browser = webdriver.Chrome()
    browser.get('https://centrodeselecao.ufg.br/fiscalizacao/sistema/confirmacao/1_confirmacao_chamada.php')

cpf = browser.find_element_by_id('cpf')
cpf.send_keys('70182005127')

acessar = browser.find_element_by_class_name('btn')
acessar.click()


try:
    confirmar_interesse = browser.find_element_by_class_name('btn-primary')
    confirmar_interesse.click()
except NoSuchElementException:
        print 'Não há concurso público disponível'
        enviar_email(email, senha)