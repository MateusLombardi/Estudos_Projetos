import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
import pandas as pd

lista_produtos = []

navegador = webdriver.Chrome()

navegador.get('https://www.mercadolivre.com.br/')

sleep(2)

pesquisa = input("Digite a pesquisa do mercado livre: ")

input_place = navegador.find_element(By.TAG_NAME, "input")
input_place.send_keys('Redmi Note')
input_place.submit()

page_content = navegador.page_source
site = BeautifulSoup(page_content, 'html.parser')

flag_pagina_seguinte = True

while flag_pagina_seguinte == True:

    produtos = site.findAll('div', attrs={'class': 'ui-search-result'})

    for produto in produtos:
        h_ref = produto.find('a')
        preco = produto.find('span', attrs={'aria-roledescription': 'Preço'})
        teste = preco['aria-label']

        lista_produtos.append([h_ref['title'], preco['aria-label'], h_ref['href']])
    try:
        btn_seguinte = navegador.find_element(By.XPATH, value="//a[@title='Seguinte']")
        navegador.execute_script("arguments[0].click();", btn_seguinte); 
        sleep(5)
    except:
        flag_pagina_seguinte = False
        pass

arq_produtos = pd.DataFrame(lista_produtos, columns=['Título', 'Preço', 'Link'])
arq_produtos.to_excel(f'{pesquisa}.xlsx', index=False)
