import requests
from bs4 import BeautifulSoup
from termcolor import colored

def scrap(apartamentos: list) -> list:
    page = requests.get("https://www.acrcimoveis.com.br/comprar/agua-verde_centro_velha_velha-central_vila-nova/apartamento"
                        "/dormitorios-2/vagas-1/valor-0_200000/ordem-recentes/resultado-decrescente/quantidade-24/")

    soup = BeautifulSoup(page.content, 'html.parser')

    for element in soup.select('div.todos_imoveis > div.resultado'):
        info = {}

        try:
            link = str("https://www.acrcimoveis.com.br"+ str(element.find('a')['href']))
        except:
            link = ""
        info['link'] = link

        try:
            titulo = str(element.select('h4.localizacao > span')[0])
            titulo = titulo.replace("<span>", "")
            titulo = titulo.replace("</span>", "")
        except:
            titulo = ""
        info['titulo'] = titulo

        try:
            valor = str(element.select('div.valor > h5')[0])
            valor = valor.replace("<h5>", "")
            valor = valor.replace("</h5>", "")
        except:
            valor = ""
        info['valor'] = valor

        try:
            descricao = str(element.select('div.detalhe > span')[0])+", "+str(element.select('div.detalhe > span')[1])\
                        +", "+str(element.select('div.detalhe > span')[2])+""+str(element.select('div.detalhe > span')[3])\
                        +", "+str(element.select('div.detalhe > span')[4])+""+str(element.select('div.detalhe > span')[5])
            descricao = descricao.replace("<span>", "")
            descricao = descricao.replace("</span>", "")
        except:
            descricao = ""
        info['descricao'] = descricao
        
        letras = "-/abcdefghijklmnoprstuvwxyz"
        try:
            cod = str(element.find('a')['href'])
            for letra in letras:
                cod = cod.replace(letra, "")
        except:
            cod = ""
        info['cod'] = cod

        apartamentos.append(info)

    print(colored("Acrc Imobiliaria ok", "green"))
    return apartamentos


# apartamentos = []
# scrap(apartamentos=apartamentos)
# print(apartamentos)