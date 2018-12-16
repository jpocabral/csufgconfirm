# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

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