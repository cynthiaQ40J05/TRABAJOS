import argparse
from papia import *
from scrip_virus_total import *
from script_enc_desc import *
from ReceiveTCP import *
from SendTCP import *

if __name__=='__main__':
    description = """ Ejemplo de uso:
            +elige una pagina web:
                -p https://www.uanl.mx/noticias/
            + selecciona la etiqueta html que desea buscar
               -p https://www.uanl.mx/noticias/  -e "h3 a"

            + para metadata de img que hay en una carpeta
                 -r C:\\Users\\user\\Desktop\\img
            + para analisis de .exe con api de virus total
                -A (su api) -pa (el path del .exe a analisar)
            +Para encriptar un .txt
                -enc (path del archivo .txt) 
            +Para desencriptar el .txt
                -des (path del .txt encriptado)
            
            ("Es importante tener dos terminales abiertas como"
            "administrador una para enviar y otra para recibir..")
                +envio de mensaje por TCP
                    -E (indique la ip de la conexion)
                    -Port (ingrese puerto ej. (-P 550))
                    -M (ingrese el mensaje a enviar)
                +resive mensaje por TCP
                    -Puerto (ingrese puerto ej. (-P 550))
    """
    
    parser=argparse.ArgumentParser(description ='Obtener los links de una pagina', epilog=description, formatter_class=argparse.RawDescriptionHelpFormatter)

    #Webscraping de una pagina web
    parser.add_argument("-p", metavar='pagina', dest="pagina",
                        help="Url de la pagina a realizar scraping")
    parser.add_argument("-e", metavar='etiqueta', dest="etiqueta",
                        help="Etiqueta html que desea buscar")
    
    #Metadata de imagenes
    parser.add_argument("-r", metavar='ruta', dest="ruta",
                        help="Directorio de imagenes para metadata")
    
    #Analizar archivo .exe con api virustotal
    parser.add_argument("-A", metavar='API', dest="API",
                        help="Coloque su api-key de virustotal")
    parser.add_argument("-path", metavar='Path', dest="Path",
                        help="Coloque el path del archivo .exe a analizar")
    #Encriptar y Desencriptar un txt
    parser.add_argument('-enc', metavar='PATH1', dest="PATH1",
                        help="Coloque el path del archivo encriptar un txt")
    parser.add_argument('-des', metavar='PATH2', dest="PATH2",
                        help="Coloque el path del archivo desencriptar un txt")
        
    #Recibir mensaje TCP
    parser.add_argument('-Puerto', metavar='Port1', dest="Port1",
                        help="Indique el puerto de la conexion")
    #Enviar mensaje TCP
    parser.add_argument('-E', metavar='EndPoint', dest="EndPoint",
                        help="Indique el ip final de la conexion")
    parser.add_argument('-Port', metavar='Port2', dest="Port2",
                        help="Indique el puerto de la conexion")
    parser.add_argument('-M', metavar='Message', dest="Message",
                        help="Indique el mensaje que desea mandar")
    params =  parser.parse_args()

    if (params.pagina is not None) and (params.etiqueta is not None ):
        pagina=params.pagina
        etiqueta=params.etiqueta
        webscraping(pagina,etiqueta)
    elif(params.ruta is not None ):
        ruta = params.ruta
        printMeta(ruta)
    elif(params.API is not None) and (params.Path is not None):
        api_key=params.API
        archivo=params.Path
        virus(api_key,archivo)
    elif(params.PATH1 is not None):
        txt=params.PATH1
        encriptar(txt)
    elif(params.PATH2 is not None):
        txt=params.PATH2
        desencriptar(txt)
    elif(params.Port1 is not None):
        puerto=params.Port1
        recibir(puerto)
    elif(params.EndPoint is not None) and (params.Port2 is not None) and (params.Message is not None):
        ip=params.EndPoint
        puerto=params.Port2
        mensaje=params.Message
        enviar(ip,puerto,mensaje)
    else:
        print("Falta de argumentos \n"+str(description))
    
