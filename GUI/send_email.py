# -*- coding: utf-8 -*-
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

def  enviar_email(email, senha, texto, assunto):

    msg = MIMEMultipart()
    msg['From'] = email
    msg['To'] = email
    msg['Subject'] = assunto

    msg.attach(MIMEText(texto,'plain'))
    #filename='teste.pdf'
    #attachment  =open(filename,'rb')

    #part = MIMEBase('application','octet-stream')
    #part.set_payload((attachment).read())
    #encoders.encode_base64(part)
    #part.add_header('Content-Disposition',"attachment; filename= "+filename)

    #msg.attach(part)
    mensagem = msg.as_string()
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(email ,senha)


    server.sendmail(email,email,mensagem)
    server.quit()
