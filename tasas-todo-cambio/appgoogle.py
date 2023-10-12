import requests
from bs4 import BeautifulSoup

#Obtener la peticion
r = requests.get('https://www.google.com/finance/quote/USD-COP')
print(r)

#Obtener la sopa con todo el contenido
soup = BeautifulSoup(r.content, 'html.parser')

#Obtener la listta de elementos deseados
elemento = soup.find(class_="YMlKec fxKbKc").text
tasa_COP_Google = float(elemento.replace(',', ''))
print(tasa_COP_Google)