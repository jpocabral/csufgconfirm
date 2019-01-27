# -*- coding: utf-8 -*-
import os, platform, subprocess
def criarServico():
    try:
        if platform.system() == 'Windows':
            print 'O sistema é Windows'
            print os.system('echo %cd%')
        elif platform.system() == 'Linux':
            servicename = 'monna.service'
            arquivo = open(servicename, "w+")
            path = subprocess.check_output('pwd', shell=True).rstrip()

            arquivo.writelines('[Unit]\n'
                               'Description=CSUFGCONFIRM\n'
                               'After=multi-user.target\n'
                               '\n'
                               '[Service]\n'
                               'Type=simple\n'
                               'ExecStart=/usr/bin/python '+path+'/main.py --cli\n'
                               '\n'
                               'Restart=always\n'
                               '[Install]\n'
                               'WantedBy=multi-user.target')

            os.system('mv '+servicename+' /lib/systemd/system/')
            os.system('sudo chmod 644 /lib/systemd/system/'+servicename)
            os.system('sudo systemctl enable '+servicename)
            os.system('sudo systemctl start '+servicename)

        elif platform.system() == 'Darwin':
            print 'A aplicação não suporta MacOS'
        else:
            print 'Sistema Operacional desconhecido.'
        return servicename
    except:
        return None