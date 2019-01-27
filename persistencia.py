# -*- coding: utf-8 -*-
import pickle

def salvar_dados(cpf, email, senha, cdpath):
    dados = {'cpf': cpf,
             'email': email,
             'senha': senha,
             'cdpath': cdpath}

    with open('dados.pickle', 'wb') as f:
        pickle.dump(dados, f, pickle.HIGHEST_PROTOCOL)

def getCpf():
    with open('dados.pickle', 'rb') as f:
        dados = pickle.load(f)
        cpf = dados['cpf']
        return cpf

def getEmail():
    with open('dados.pickle', 'rb') as f:
        dados = pickle.load(f)
        email = dados['email']
        return email

def getSenha():
    with open('dados.pickle', 'rb') as f:
        dados = pickle.load(f)
        senha = dados['senha']
        return senha

def getCdpath():
    with open('dados.pickle', 'rb') as f:
        dados = pickle.load(f)
        cdpath = dados['cdpath']
        return cdpath

def primeiraVez():
    try:
        with open('dados.pickle', 'rb') as f:
            return False
    except IOError:
        return True
