import requests
from bs4 import BeautifulSoup

#Obtener la peticion
r = requests.get('https://www.bcv.org.ve/')
print(r)

#Obtener la sopa con todo el contenido
soup = BeautifulSoup(r.content, 'html.parser')

#Obtener la listta de elementos deseados
elementos = soup.find_all(class_="col-sm-6 col-xs-6 centrado")
tasa_bcv = float(elementos[4].text.replace(' ', '').replace(',', '.'))
print(tasa_bcv)