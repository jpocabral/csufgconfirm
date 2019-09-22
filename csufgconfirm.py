from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from send_email import enviar_email
from time import sleep

def iniciar(cpf, email_origem, email_destino, senha):

    url = 'https://centrodeselecao.ufg.br/fiscalizacao/sistema/confirmacao/1_confirmacao_chamada.php'


    while True:
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--window-size=1420,1080')
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        browser = webdriver.Chrome("/usr/bin/chromedriver",chrome_options=chrome_options)

    # Acessa o site
        browser.get(url)

        # Autenticação
        campocpf = browser.find_element_by_id('cpf')
        campocpf.send_keys(cpf)
        acessar = browser.find_element_by_class_name('btn')
        acessar.click()

        # Visualiza concursos disponíveis
        try:
            confirmar_interesse = browser.find_element_by_class_name('btn-primary')
            confirmar_interesse.click()

            # Caso haja concursos disponíveis
            print ('Ha concursos publicos disponiveis!')
            enviar_email(email_origem, email_destino, senha, texto="Mais informações em "+url, assunto="UFG - Novo concurso disponível!")

            #Dormir Por 2 dias
            sleep(172800)

        #Caso não haja concurso disponível
        except NoSuchElementException:
            print ('Nao ha concurso publico disponivel!')
        browser.quit()
        sleep(900)

iniciar(cpf="99999999999",email_origem="seuemail@dominio.com",email_destino="emaildestino@dominio.com",senha="senha_do_email")

