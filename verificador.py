#!/usr/bin/env python
import sqlite3
import subprocess

def acharBanco():
    print("Aqui terá a função que encontrará o caminho do banco de dados SQLite do usuário")


def pesquisarBanco(pesquisa):
    conn = sqlite3.connect(acharBanco())
    c = conn.cursor()
    link = c.execute("SELECT * FROM tabela_q_esqueci_o_nome WHERE variável = ?", pesquisa)

def baixarCheck(link):
    subprocess.call(["wget", "-f", link])

# Talvez vou usar essa função
def md5Arquivo(arquivo):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

# Criar função que gerará o md5 ou seja lá qual for o negócio e comparar com o baixado pela função baixarCheck()
def verificarCheck(arquivo, checksum):

