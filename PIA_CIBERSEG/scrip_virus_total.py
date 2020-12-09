from hashlib import md5
import os
from virus_total_apis import PublicApi
import argparse

##"Analisis de archvios .exe con Virus Total API"+\
##"Debe ingresar la api de virus total,cree una cuenta en:
##"https://www.virustotal.com/gui/"

##try:
##    import md5
##except ImportError:
##    print('se intalara modulo faltante')
##    os.system('pip install md5')
##    print('ejecuta de nuevo el script')
##    exit()
##try:
##    import PublicApi
##except ImportError:
##    ('se instalara modulo faltante')
##    os.system('pip install virustotal-api')
##    print('ejecute de nuevo el script')
##    exit()

def virus(api_key,archivo):
    api= PublicApi(api_key)
    with open(archivo, "rb") as f:
        file_hash=md5(f.read()).hexdigest()
    response= api.get_file_report(file_hash)
    if response["response_code"] == 200:
        if response["results"]["positives"] > 0:
            print("Es un archivo MALICIOSO, AGUAS!")
        else:
            print("Es un archivo SEGURO")
    else:
        print('No ha podido obtenerse el analisis del archivo')
