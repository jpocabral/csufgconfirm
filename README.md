# CSUFGCONFIRM

O projeto se trata de um script automático em python que faz uso da biblioteca de automação web Selenium e o ChromeDriver afim de automatizar o processo de confirmação do interesse do fiscal do Centro de Seleção UFG nos concursos públicos disponíveis, ajudando os mesmos a se manterem atualizados visto que o próprio website não envia notificações aos usuários ocasionando na falta de profissionais em vários concursos ministrados. 

# Exemplo de uso:
- Editar as variáveis de csufgconfirm.py
- docker build -t csufgconfirm .
- docker run -d --name csufgconfirm csufgconfirm
