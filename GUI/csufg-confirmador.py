from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://centrodeselecao.ufg.br/fiscalizacao/sistema/confirmacao/1_confirmacao_chamada.php')

cpf = browser.find_element_by_id('cpf')
cpf.send_keys('70182005127')

acessar = browser.find_element_by_class_name('btn')
acessar.click()

next = browser.find_element_by_class_name('btn-primary')
next.click()
