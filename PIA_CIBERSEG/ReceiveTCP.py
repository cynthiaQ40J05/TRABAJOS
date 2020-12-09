import subprocess
import argparse
import os

##'Receive-TCPMessage with PowerShell, -version 1.0 December 2020'


def recibir(puerto):
    try:
        '''Execution PowerShell'''
        command = "powershell -ExecutionPolicy ByPass -File ReceiveTCP.ps1 -Port " + puerto
        print(command)
        powerShellResult = subprocess.run(command, stdout=subprocess.PIPE)
        if powerShellResult.stderr == None:
            print(powerShellResult.stdout.decode('ascii'))
        else:
            print("Powershell Error:", p.stderr)
    except Exception as err:
        print ("Cannot Create Output File: "+str(err))
        quit()

##if __name__ == "__main__":
##    recibir()
