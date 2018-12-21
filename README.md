# CSUFGCONFIRM

O projeto se trata de um script automático em python que faz uso da biblioteca de automação web Selenium e o ChromeDriver afim de automatizar o processo de confirmação do interesse do fiscal do Centro de Seleção UFG nos concursos públicos disponíveis, ajudando os mesmos a se manterem atualizados visto que o próprio website não envia notificações aos usuários ocasionando na falta de profissionais em vários concursos ministrados. 

# Instalando dependências:
- sudo apt-get install python python-pip
- pip install selenium
- [Chromedrive](http://chromedriver.chromium.org)
- [Google Chrome](https://www.google.com/chrome/) ou [Chromium](https://www.chromium.org/getting-involved/download-chromium)
- [Gerar senha de App - Email](https://security.google.com/settings/security/apppasswords) (Para maior segurança do usuário ao enviar os email's de notificação)

# Exemplos de uso:
- python csufgconfirm.py --cpf 11111111111 --email seuemail@gmail.com --senha senha --cdpath C:\\PROGRA~1\Chromedriver\chromedriver.exe
- python csufgconfirm.py --cli --cpf 11111111111 --email seuemail@gmail.com --senha senha --cdpath /usr/lib/chromium-browser/chromedriver
