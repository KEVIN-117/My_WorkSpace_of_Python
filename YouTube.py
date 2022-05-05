from io import open
import urllib.request
from bs4 import BeautifulSoup
from nbformat import read
datos = urllib.request.urlopen('https://clinic-cloud.com/blog/20-frases-celebres-sobre-ciencia-citas-cientificas/').read().decode()
soup = BeautifulSoup(datos)
tags = soup('em')
archivo = open("python\contenedor.txt", "w")
for tag in tags:
    archivo.write(tag.text+"\n")
archivo.close()