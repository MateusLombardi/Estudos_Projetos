import requests 
from bs4 import BeautifulSoup

response= requests.get('https://www.uol.com.br/')

conteudo= response.content

site= BeautifulSoup(conteudo,'html.parser')

#noticia
noticia= site.find('div', attrs={'class':'title__element headlineMain__title'})

titulo = noticia.find('a', attrs={'class': 'title__element headlineMain__title'})

print(titulo.text)