# Faz um request de uma API de livros do Stephen King e capta informações de acordo com o input do usuário

import requests
import json

def consulta_livros(lista_livros):
    print('Essa é uma lista de livros escritos por Stephen King! O que você quer consultar?\n********************')
    entrada = input('-> nomes\n-> ano das publicações\n-> número de páginas\n-> sair\n')
    
    while (entrada != 'sair'):
        if (entrada == 'nomes'):
            print('\n')
            for books in dict:
                print('-> ', books['Title'])
        elif (entrada == 'ano das publicações'):
            print('\n')
            for books in dict:
                print('-> ', books['Title'], '(', books['Year'], ')')
        elif (entrada == 'número de páginas'):
            print('\n')
            for books in dict:
                print('-> ', books['Title'], ': ', books['Pages'], 'páginas')
        entrada = input('\nO que você quer consultar?\n********************\n-> nomes\n-> ano\n-> páginas\n-> sair\n')

req = None
try:
    req = requests.get("https://stephen-king-api.onrender.com/api/books/")
    dict = json.loads(req.text)
    dict = dict['data']
    consulta_livros(dict)

except Exception as error:
    print("Requisição inválida: ", error)
    exit()