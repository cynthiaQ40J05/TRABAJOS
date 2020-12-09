import subprocess
import argparse
import os

##"Send-TCPMessage with PowerShell, -version 1.0 December 2020'

def enviar(ip,puerto,mensaje):
    msj = (f'"{mensaje}"')
    try:
        '''Execution PowerShell'''
        command = "powershell -ExecutionPolicy ByPass -File SendTCP.ps1 -EndPoint "+\
                  ip + " -Port " + puerto + " -Message " + msj
        print(command)
        powerShellResult = subprocess.run(command, stdout=subprocess.PIPE)
        if powerShellResult.stderr == None:
            print("Mensaje enviado exitosamente!!")
        else:
            print("Powershell Error:", p.stderr)
    except Exception as err:
        print ("Cannot Create Output File: "+str(err))
        quit()

##if __name__ == "__main__":
##    enviar()
