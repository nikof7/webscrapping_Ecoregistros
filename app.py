import requests
from bs4 import BeautifulSoup
import webbrowser

base_url = "https://www.ecoregistros.org"

sp = 'Alectoris-chukar'

def buscar_n_registros(name):
	url = base_url + '/ficha/' + name
	r = requests.get(url)
	soup = BeautifulSoup(r.content,'html.parser')
	n_registros = str(soup.find_all('span', class_='tamanioPequenio colorFuenteDescripcion center')[4])
	return n_registros[86:-11]

def abrir_img_registro(id):
	url_by_id = base_url + "/site/imagen.php?id=" + id
	r = requests.get(url_by_id)
	soup = BeautifulSoup(r.content,'html.parser')

	# Busca en el html 'img'
	imagen = soup.find_all('img')
	#imagen[1] corresponde al lugar donde siempre se encuentra el src de la imagen a buscar
	img_src = str(imagen[1]).split('"')
	# crea el link con la base_url y
	link_imagen = base_url + img_src[5][2:]

	return webbrowser.open(link_imagen, new=1)

def id_ultima_img(taxa):
	url = base_url + '/ficha/' + taxa

	r = requests.get(url)

	soup = BeautifulSoup(r.content,'html.parser')

	# El [0] busca solo el primer elemento, el de fotografía, hay otro elemento que es de video
	div_con_datos = soup.find_all('div', style='width:300px;height:390px;margin-left:20px;margin-right:20px;float:center;display:inline-block;vertical-align:top')[0]

	forma_lista = div_con_datos.text.split(' ')

	id_final = forma_lista[2].split("\xa0")[0]

	return(id)


print(id_ultima_img('Alectoris-chukar')