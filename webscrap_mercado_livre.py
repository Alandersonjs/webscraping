#busca automatizada

import requests
from bs4 import BeautifulSoup
from PIL import Image
from io import BytesIO

url_base = 'https://lista.mercadolivre.com.br/'

produto_nome = input('Qual produto você deseja? ')

response = requests.get(url_base + produto_nome)

site = BeautifulSoup(response.text, 'html.parser')

produtos = site.find_all('div', attrs={'class':'andes-card ui-search-result ui-search-result--core andes-card--flat andes-card--padding-16'})

for produto in produtos:
    titulo = produto.find('h2', attrs={'class': 'ui-search-item__title'})
    link = produto.find('a', attrs={'class': 'ui-search-link'})
    
    real = produto.find('span', attrs={'class': 'andes-money-amount__fraction'})
    centavos = produto.find('span', attrs={'class': 'andes-money-amount__cents andes-money-amount__cents--superscript-24'})

# Verifica se os elementos necessários foram encontrados
    if titulo is not None and link is not None and real is not None:
        # Convertendo o preço para um valor numérico
        preco = float(real.text.replace('.', '').replace(',', '.'))  # Substitui vírgulas por pontos e converte para float
        # Verifica se o preço é menor que 30 reais
    if preco < 30:
        #print(produto.prettify())
        print('Titulo do produto:', titulo.text)
        print('Link do produto:', link['href'])
        print('Preço do produto: R$', real.text + ',' + centavos.text)
        print('\n\n')