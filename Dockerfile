FROM ubuntu:18.04

#Atualizar
RUN apt-get update -y

#Instalar Chromium
RUN apt-get install chromium-browser -y

#Instalar Programas
RUN apt-get install python3 -y
RUN apt-get install python3-pip -y
RUN apt-get install unzip -y
RUN apt-get install apt-utils -y
RUN apt-get install wget -y

#Instalar Selenium
RUN pip3 install selenium

#Adicionar arquivos
ADD csufgconfirm.py /
ADD send_email.py /

#Instalar Chromedriver
ADD chromedriver /usr/bin/

#Executar o Programa
CMD [ "python3", "-u" , "/csufgconfirm.py" ]

