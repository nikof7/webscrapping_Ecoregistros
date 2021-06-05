import requests
from bs4 import BeautifulSoup

scientific_name = "Alectoris-chukar"

url = 'https://www.ecoregistros.org/ficha/' + scientific_name

r = requests.get(url)

soup = BeautifulSoup(r.content,'html.parser')

n_registros = str(soup.find_all('span', class_='tamanioPequenio colorFuenteDescripcion center')[4])

print(n_registros[86:-11])