import requests

response = requests.get('https://www.mercadolivre.com.br/')

print('Status code:', response.status_code)
print(' \nConteúdo da página: ')
print(response.content)