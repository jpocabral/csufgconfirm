from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--window-size=1420,1080')
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
chrome_options.binary_location = '/usr/bin/chromium-browser'

service_log_path = "{}/chromedriver.log".format('/home/pi')

browser = webdriver.Chrome('/usr/lib/chromium-browser/chromedriver',
			  chrome_options=chrome_options,
			  service_log_path=service_log_path)
browser.get('https://centrodeselecao.ufg.br/fiscalizacao/sistema/confirmacao/1_confirmacao_chamada.php')

cpf = browser.find_element_by_id('cpf')
cpf.send_keys('70182005127')

acessar = browser.find_element_by_class_name('btn')
acessar.click()

