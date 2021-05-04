import requests
from bs4 import BeautifulSoup


page = requests.get('https://www.blumenauimoveis.com.br/imoveis?pretensao=comprar&tipos=1&cidade=4202404&bairros=30579%2C30552%2C30578%2C30573%2C36166%2C30576&valor_min=0&valor_max=200.000&ordem=menor-valor')

soup = BeautifulSoup(page.content, 'html.parser')

apartamentos = []

for element in soup.select('div.block-imoveis-list > div.row > div.col-12'):
    info = {}
    try:
        link = str("https://www.blumenauimoveis.com.br/"+str(element.find('a')['href']))
    except:
        link = ""
    info['link'] = link

    try:
        titulo = str(element.select('div.titulo-imovel-lista > h3')[0])
        titulo = titulo.replace("<h3>", "")
        titulo = titulo.replace("</h3>", "")
    except:
        titulo = ""

    info['titulo'] = titulo

    try:
        valor = str(element.select('div.valor-imovel-lista > span')[0])
        valor = valor.replace("<span>", "")
        valor = valor.replace("</span>", "")
    except:
        valor = ""
    info['valor'] = valor

    try:
        descricao = str(element.select('div.desc-curta-imovel-lista > h6')[0])
        descricao = descricao.replace("<h6>", "")
        descricao = descricao.replace("</h6>", "")
    except:
        descricao = ""
    info['descricao'] = descricao

    try:
        cod = str(element.select('div.cod-pret-imovel-lista> span')[1])
        cod = cod.replace("<span>", "")
        cod = cod.replace("</span>", "")
        cod = cod.replace("Cód. ", "")
    except:
        cod = ""
    info['cod'] = cod

    apartamentos.append(info)

for ap in apartamentos:
    print("Link: ", ap['link'])
    print("Titulo: ", ap['titulo'])
    print("Valor: ", ap['valor'])
    print("Descrição: ", ap['descricao'])
    print("Código: ", ap['cod'])
    print('-------------------')
