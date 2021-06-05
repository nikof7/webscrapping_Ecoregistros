import requests
from bs4 import BeautifulSoup

scientific_name = "Alectoris-chukar"

url = 'https://www.ecoregistros.org/ficha/' + scientific_name

r = requests.get(url)

soup = BeautifulSoup(r.content,'html.parser')

# El [0] busca solo el primer elemento, el de fotografía, hay otro elemento que es de video
div_con_datos = soup.find_all('div', style='width:300px;height:390px;margin-left:20px;margin-right:20px;float:center;display:inline-block;vertical-align:top')[0]

forma_lista = div_con_datos.text.split(' ')

id_final = forma_lista[2].split("\xa0")[0]

print(id_final)