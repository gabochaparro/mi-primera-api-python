from flask import Flask, jsonify
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

app = Flask(__name__)

# Ruta que devuelve un número
@app.route('/tasa', methods=['GET'])
def obtener_numero():
    numero = tasa_bcv  # Puedes cambiar este número por el que desees
    return jsonify({'tasa': numero})

if __name__ == '__main__':
    app.run(debug=True)
