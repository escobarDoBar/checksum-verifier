#!/usr/bin/env python
import sqlite3
import subprocess

def acharBanco():
    print("Aqui terá a função que encontrará o caminho do banco de dados SQLite do usuário")


def pesquisarBanco(pesquisa):
    conn = sqlite3.connect(acharBanco())
    c = conn.cursor()
    link = c.execute("SELECT linkDownload FROM tabela_q_esqueci_o_nome WHERE variável = ?", pesquisa) # Tabela, coluna e variavel possuem esses nomes porque esqueci seus nomes reais :)

def baixarCheck(link):
    # Realizar modificação no link para retornar pelo menos 1 diretório para realizar a pesquisa dos arquivos disponíveis
    # link = {código que vai fazer isso}
    links = subprocess.call(["goofile ", "-d ", link, " -f ", "txt ", "| ", "grep ", "txt"]) # Realizar mais de uma pesquisa caso necessário
    # Serão quebrados os links encontrados para o usuário conseguir escolher de quais deles deseja baixar, caso haja apenas um link o usuário não terá a opção de escolha

    # Loop feito que realizará a exibição do links
    y = 1
    for x in links:
        print(y, ") ", x)
        y += 1

    # Tenho que descobrir qual tipo de Python usarei e então escolher qual dos dois inputs vou usar
    opcao = raw_input('Enter your input:')  # If you use Python 2
    opcao = input('Enter your input:')      # If you use Python 3

    # Salva o link conforme a escolha do usuário
    y = 1
    for x in links:
        if y == opcao:
            link = x
        y += 1

    # Baixa o arquivo para realziar a verificação
    subprocess.call(["wget", "-f", link])

# Talvez vou usar essa função
def md5Arquivo(arquivo):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

# Criar função que gerará o md5 ou seja lá qual for o negócio e comparar com o baixado pela função baixarCheck()
def verificarCheck(checksum):
    subprocess.call(["sha256sum", "-c", checksum])
    # Printar o resultado da verificação

# Função principal que rodará o programa
def main():

    # Descobre o link do checksum e baixa ele
    link = pesquisarBanco($0)
    baixarCheck(link)

    # Verifica o checksum
    verificarCheck(variavelOpção)
    

