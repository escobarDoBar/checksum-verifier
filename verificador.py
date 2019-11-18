#!/usr/bin/env python
import sqlite3
import subprocess
import sys
import getopt
import csv

def acharBanco():
    return banco = "~/banco.sqlite"


def pesquisarBanco(pesquisa):
    conn = sqlite3.connect(acharBanco())
    c = conn.cursor()
    link = c.execute("SELECT linkDownload FROM cacheDownload WHERE arquivo = ?", pesquisa) # Tabela, coluna e variavel possuem esses nomes porque esqueci seus nomes reais :)
    return link

def baixarCheck(pesquisa):
    http,link,resto = pesquisa.slipt("/", 3)
    linkPesquisa = http+"//"+link
    
    links = subprocess.run(["goofile", "-d", linkPesquisa, "-f", "gpg", "|", "grep", "gpg", ">", "/tmp/links.txt"]) # Realizar mais de uma pesquisa caso necessário
    
    f = open('/tmp/links.txt', 'r')
    links = f.readlines()
    f.close()
    # Serão quebrados os links encontrados para o usuário conseguir escolher de quais deles deseja baixar, caso haja apenas um link o usuário não terá a opção de escolha
    # Falta fazer a linha de cima

    # Loop feito que realizará a exibição do links
    y = 1
    for x in links:
        print(y+") "+x)
        y += 1

    opcao = input('Coloque o número realacionado ao link que desejas baixar: ')

    # Salva o link conforme a escolha do usuário
    y = 1
    for x in links:
        if y == opcao:
            linkGPG = x
        y += 1

    

    # Baixa o arquivo para realziar a verificação
    sucessoGPG = subprocess.run(["wget", "-o", "verificar.gpg", "-f", link])
    if sucessoGPG == 0:    
        print("Arquivo GPG baixado com sucesso")
    else:
        print("Houve um erro ao baixar o arquivo GPG")

    linkSHA = linkGPG.slipt(".gpg")
    sucessoSHA = subprocess.run(["wget", "-o", "sha256sum.txt", "-f", linkSHA])
    if sucessoSHA == 0:    
        print("Arquivo SHA baixado com sucesso")
    else:
        print("Houve um erro ao baixar o arquivo SHA")

def verificarCheck(checksum):
    print(subprocess.run([(["sha256sum", "-c", checksum], capture_output=True)

# Função principal que rodará o programa
def main():

    try:
      opts, args = getopt.getopt(argv,"hc:",["check="])
    except getopt.GetoptError as err:
      print(err)  
      print('Forma de usar: verificador.py -c arquivo_baixado')
      sys.exit(2)
    for opt, arg in opts:
      if opt == '-h':
         print('verificador.py -c arquivo_baixado')
         sys.exit()
      elif opt in ("-c", "--check"):
         arquivo = arg

    # Descobre o link do checksum e baixa ele
    link = pesquisarBanco(arquivo)
    baixarCheck(link)

    # Verifica o checksum
    verificarCheck("sha256sum.txt")