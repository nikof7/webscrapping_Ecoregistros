import requests
from bs4 import BeautifulSoup
import webbrowser

# Busca un registro por ID.

base_url = "https://www.ecoregistros.org"

id = str(446286)

url_by_id = base_url + "/site/imagen.php?id=" + id

r = requests.get(url_by_id)

soup = BeautifulSoup(r.content,'html.parser')

# Busca en el html 'img'
imagen = soup.find_all('img')

#imagen[1] corresponde al lugar donde siempre se encuentra el src de la imagen a buscar
img_src = str(imagen[1]).split('"')

# crea el link con la base_url y
link_imagen = base_url + img_src[5][2:]

webbrowser.open(link_imagen, new=1)