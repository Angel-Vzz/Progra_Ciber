import requests
import os
import sys
from bs4 import BeautifulSoup as bs
try: 
    import webbrowser
    
except ImportError: 

    os.system('pip install webbrowser') 
    print('Installing webbrowser...') 
    print('Ejecuta de nuevo tu script...') 
    exit() 
#Angel Alejandro Vázquez García
print("Este script navega en las páginas de noticas de la UANL")
inicioRango = int(input("Pagina inicial para buscar: "))
finRango = int(input("Pagina final para buscar: "))
dependencia = input("Ingrese las siglas de la Facultad a buscar: ")
if inicioRango > finRango: # Este pequeño bloque se encarga de que los parametros sean correctos en cuanto a mayor y menor
    inicioRango,finRango = finRango,inicioRango
for i in range (inicioRango,finRango,1):#Este bloque recorre las paginas indicadas del link
    url = "https://www.uanl.mx/noticias/page/"+str(i)
    pagina = requests.get (url)
    if pagina.status_code != 200:
        raise TypeError("Pagina no encontrada")
    else:
        soup = bs(pagina.content,"html.parser")
        info = soup.select("h3 a")
        for etiqueta in info: # Busca coincidencias en las paginas buscadas
            url2 = etiqueta.get("href")
            pagina2 = requests.get(url2)
            if pagina2.status_code == 200:
                soup2 = bs(pagina2.content,"html.parser")
                parrafos = soup2.select("p")    
                for elemento in parrafos:
                    if dependencia in elemento.getText():
                        print ("Abriendo",url2) # Abre las URL con resultados positivos
                        webbrowser.open(url2)
                        break
    
