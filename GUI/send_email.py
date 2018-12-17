# -*- coding: utf-8 -*-
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

def  enviar_email(usuario, senha, destinatario):

    subject = 'UFG - Concurso Confirmado'

    msg = MIMEMultipart()
    msg['From'] = usuario
    msg['To'] = destinatario
    msg['Subject'] = subject

    body = 'Hi there, sending this email from Python!'
    msg.attach(MIMEText(body,'plain'))
    filename='teste.pdf'
    attachment  =open(filename,'rb')

    part = MIMEBase('application','octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition',"attachment; filename= "+filename)

    msg.attach(part)
    text = msg.as_string()
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(usuario ,senha)


    server.sendmail(usuario,destinatario,text)
    server.quit()
