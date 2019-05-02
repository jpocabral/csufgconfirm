# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from send_email import enviar_email
import time

def iniciar(cpf, email, senha, cdpath, modo):

    url = 'https://centrodeselecao.ufg.br/fiscalizacao/sistema/confirmacao/1_confirmacao_chamada.php'

    if modo is 'GUI' or modo is 'gui':
        print ('MODO GUI')
        while True:
            browser = webdriver.Chrome(cdpath)
            browser.get(url)

            #AUTENTICAÇÃO
            campocpf = browser.find_element_by_id('cpf')
            campocpf.send_keys(cpf)
            acessar = browser.find_element_by_class_name('btn')
            acessar.click()

            #VISUALIZA CONCURSOS DISPONÍVEIS
            try:
                confirmar_interesse = browser.find_element_by_class_name('btn-primary')
                confirmar_interesse.click()

                # TRATAMENTO DE CONCURSOS DISPONÍVEIS
                print ('Há um concurso público disponível')
                enviar_email(email, senha, texto="Mais informações em " + url, assunto="UFG - Novo concurso disponível!")
            except NoSuchElementException:
                    print ('Não há concurso público disponível')
            browser.quit()
            time.sleep(30)

    elif modo is 'CLI' or modo is 'cli':
        while True:
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument('--no-sandbox')
            chrome_options.add_argument('--window-size=1420,1080')
            chrome_options.add_argument('--headless')
            chrome_options.add_argument('--disable-gpu')

            browser = webdriver.Chrome(cdpath,chrome_options=chrome_options)

            browser.get(url)
            # AUTENTICAÇÃO
            campocpf = browser.find_element_by_id('cpf')
            campocpf.send_keys(cpf)
            acessar = browser.find_element_by_class_name('btn')
            acessar.click()

            # VISUALIZA CONCURSOS DISPONÍVEIS
            try:
                confirmar_interesse = browser.find_element_by_class_name('btn-primary')
                confirmar_interesse.click()

                # TRATAMENTO DE CONCURSOS DISPONÍVEIS
                print ('Há concursos públicos disponíveis')
                enviar_email(email, senha, texto="Mais informações em "+url, assunto="UFG - Novo concurso disponível!")
            except NoSuchElementException:
                print ('Não há concurso público disponível')
            browser.quit()
            time.sleep(30)