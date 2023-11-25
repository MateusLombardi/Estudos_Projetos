
# > EXEMPLO
# - Obtendo produtos do Mercado Livre a partir de uma busca realizada pelo usuário

import requests
from bs4 import BeautifulSoup

url_base = 'https://lista.mercadolivre.com.br/'

produto_nome = input('Qual produto você deseja? ')

response = requests.get(url_base + produto_nome)

site = BeautifulSoup(response.text, 'html.parser')

produtos = site.findAll('div', attrs={'class': 'ui-search-result__content'})

for produto in produtos:
    titulo = produto.find('href', attrs={'class':'ui-search-result__content'})
    link = produto.find('a', attrs={'class': 'ui-search-link'})

    real = produto.find('span', attrs={'class': 'price-tag-fraction'})
    centavos = produto.find('span', attrs={'class': 'price-tag-cents'})

    print(produto.prettify())
    print('Título do produto:', titulo.text)
    print('Link do produto:', link['href'])

    if (centavos):
        print('Preço do produto: R$', real.text + ',' + centavos.text)
    else:
        print('Preço do produto: R$', real.text)
    
    print('\n\n')
    break



