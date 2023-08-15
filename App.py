import os
import pickle
import datetime
import random

def menuPrincipal():
    print("|"*40)

    
    while True:
        
        entrada =input()

        if(entrada.startswith('execute')):    
            disolv = entrada.split()
            comando=disolv[0]
            path= disolv[1]              
            print(comando)  
            print(path)
        if(entrada.startswith('mkdisk')):
            fecha = datetime.datetime.now().date()
            hora = datetime.datetime.now().time()
            horaActual = hora.strftime('%H:%M')
            fechaActual=fecha.strftime('%d-%m-%Y')
            print(fechaActual, horaActual)
            numRandom = random.randrange(100, 999,1)
            print(numRandom)
        if(entrada.startswith('rep')):
            print("ingreso REP")            
        else:
            print("comando incorrecto")


if __name__=="__main__":
   menuPrincipal()