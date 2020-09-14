import os
import sys
try:
    import webbrowser
    import requests
    from bs4 import BeautifulSoup as bs
except ImportError:
    os.system("pip install webbrowser")
    os.system("pip install requests")
    os.system("pip install BeautifulSoup")
    
# CYNTHIA PATRICIA SANDOVAL MENDOZA
# En este codigo como dice al principio navega en las noticias de la uanl,
# para eso le pedimos el rango de inicio de paginas, en donde quiere empezar y
# donde quiere terminar, asi para poder dar por hecho que de cualquier forma que las acomode,
# esto las pondra de tal forma de que se pueda realizar la busqueda en esas paginas.
# Despues para cada pagina que se vaya a buscar se crea una variable url donde sta el link de
# la pagina de noticias de la uanl y se le agrega el numero de pagina, tambien se hace
# un request a el link y si el el estatus de la pagina es diferente de 200, se le imprime
# al usuario que la pagina no fue encontrada y si no es asi entonces sacamos el contenido,
# haciendo un parseo y ademas de uso poniendolo en formato bonito, creamos una variable
# donde seleccionaremos lo que tenga esa etiqueta con el encabezado h3, despues hacemos un para,
# cada etiqueta  que este en la variable info, obtenemos todas los links y tambien
# hacemos un request a esos mismos links y checamos si al hacer un request el estatus nos sale,
# identico a 200 entonces tenemos otra variable donde sacamos el contenido del request anteriormente
# realizado, se le hace un parseo y se pone en forma bonita; tambien creamos una variable en el cual
# seleccionamos los parrafos por medio de una etiqueta, y para cada elemento que se encuentre en los
# parrafos , si las siglas estan en el texto de texto, se le muestra al usuario "abriendo, el linkque sea"
# y se abre la pagina web.
    
print("Este script navega en las páginas de noticas de la UANL")
inicioRango = int(input("Pagina inicial para buscar: "))
finRango = int(input("Pagina final para buscar: "))
dependencia = input("Ingrese las siglas de la Facultad a buscar: ")
if inicioRango > finRango:
    inicioRango,finRango = finRango,inicioRango
for i in range (inicioRango,finRango,1):
    url = "https://www.uanl.mx/noticias/page/"+str(i)
    pagina = requests.get (url)
    if pagina.status_code != 200:
        raise TypeError("Pagina no encontrada")
    else:
        soup = bs(pagina.content,"html.parser")
        info = soup.select("h3 a")
        for etiqueta in info:
            url2 = etiqueta.get("href")
            pagina2 = requests.get(url2)
            if pagina2.status_code == 200:
                soup2 = bs(pagina2.content,"html.parser")
                parrafos = soup2.select("p")    
                for elemento in parrafos:
                    if dependencia in elemento.getText():
                        print ("Abriendo",url2)
                        webbrowser.open(url2)
                        break



