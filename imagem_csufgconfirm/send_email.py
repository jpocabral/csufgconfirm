# -*- coding: utf-8 -*-

from smtplib import SMTP,SMTPAuthenticationError, SMTPSenderRefused
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def  enviar_email(email_origem, email_destino, senha, texto, assunto):

    msg = MIMEMultipart()
    msg['From'] = email_origem
    msg['To'] = email_destino
    msg['Subject'] = assunto

    msg.attach(MIMEText(texto,'plain'))

    mensagem = msg.as_string()
    server = SMTP('smtp.gmail.com',587)
    server.starttls()
    try:
        server.login(email_origem, senha)
        server.sendmail(email_origem,email_destino,mensagem)
        print("Email enviado!")
    except SMTPAuthenticationError:
        print("Senha do email incorreta!")

    server.quit()
