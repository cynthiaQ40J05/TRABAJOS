## script para encriptar un archivo de texto y desencriptar un archivo###
from cryptography.fernet import Fernet

def encriptar(txt):
    def genera_clave():
        clave=Fernet.generate_key()
        with open("clave.key","wb") as archivo_clave:
            archivo_clave.write(clave)
    #funcion para cargar clave       
    def carga_clave():
        return open("clave.key","rb").read()
    #funcion para encriptar archivo
    def encript(txt,clave):
        f=Fernet(clave)
        with open(txt,"rb") as file:
            archivo_info=file.read()
        encrypted_data= f.encrypt(archivo_info)
        with open(txt,"wb") as file:
            file.write(encrypted_data)

    #funcion para desencriptar
    def desencript(txt,clave):
        f=Fernet(clave)
        with open(txt,"rb") as file:
            encrypted_data=file.read()
        decrypted_data=f.decrypt(encrypted_data)
        with open (txt,"wb") as file:
            file.write(decrypted_data)

    genera_clave()      
    clave=carga_clave()
    encript(txt, clave)
    

def desencriptar(txt):
    def genera_clave():
        clave=Fernet.generate_key()
        with open("clave.key","wb") as archivo_clave:
            archivo_clave.write(clave)
    #funcion para cargar clave       
    def carga_clave():
        return open("clave.key","rb").read()
    #funcion para encriptar archivo
    def encript(txt,clave):
        f=Fernet(clave)
        with open(txt,"rb") as file:
            archivo_info=file.read()
        encrypted_data= f.encrypt(archivo_info)
        with open(txt,"wb") as file:
            file.write(encrypted_data)

    #funcion para desencriptar
    def desencript(txt,clave):
        f=Fernet(clave)
        with open(txt,"rb") as file:
            encrypted_data=file.read()
        decrypted_data=f.decrypt(encrypted_data)
        with open (txt,"wb") as file:
            file.write(decrypted_data)

    #genera_clave()      
    clave=carga_clave()
    desencript(txt,clave)



