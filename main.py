import os
import sys
from pathlib import Path
from mbr import mbr
import pickle
#path = '/home/ugab/Documentos/GitHub/MIA-Tarea2_201213010/archivo.adsj'

def Menu():

    while True:
        print("\n")
        print("Gabriel Orlando Ajsivinac Xicay 201213010")
        print("Ingrese  comando\n")
        orden = input("")

        if(orden.startswith('execute')):
            arreglo = orden.split()
            palabra = arreglo[0]
            ruta0 = arreglo[1]
            
            ruta = ruta0
    
            path = f'{ruta}'
            path1 = f"{ruta}"
            #path = '/home/ugab/Documentos/GitHub/MIA-Tarea2_201213010/archivo.adsj'
    
            if Path(path).is_file():
                
                print('el archivo SI existe')
                print("...")
                contador1 = 0
                archivo ='inicialMBR.adsj'
                archivo1="inicialMBR.adsj"
                palabra1 = 'mkdisk'
                palabra2 = 'rep'

                with open(path1) as archivo:
                    for linea in archivo:

                        archivo ='inicialMBR.adsj'
                        if palabra1 == linea.strip():
                            print(linea)
                            print("")
                        # Se crea el archivo   
                            try:
                                fileOpen = open(archivo, "wb")  # Open the file in write mode
                                print("Archivo creado exitosamente")
        
                            except Exception as e:
                                print(f"Error creating the file: {e}")

                        # se llena el archivo 
                            #mb to bytes -> mb * 1024kb/1mb * 1024b/1kb -> mb * 1024 * 1024
                            try:    
                                buffer = b'\0'*1024
                                times_to_write =  5  * 1024 

                                for i in range(times_to_write):
                                    fileOpen.write(buffer)

                                print("Archivo llenado exitosamente")
                
                            except Exception as e:
                                print(f"Error llenando el archivo")  
                            print("")
                        # Si la palabra es rep  
                        if palabra2 == linea.strip():
                            try:
                                print(linea.strip())
                                print("")
                                mbr1 = mbr()
                                mbr1.set_information(527,'15/1/2023', 1)
                            
                            #Se Escribe en el archivo el registro en binario
                                data_serializada = pickle.dumps(mbr1)
                                abrir_archivo = open(archivo1, "rb+") # lectura y escritura binaria
                                abrir_archivo.write(data_serializada)
                                abrir_archivo.close()
                            #Se Lee el archivo binario y se muestra el registro
                                abrir_archivo = open(archivo1, "rb+") 
   
                                person_obj_recuperado = mbr()

                                data_serializada_recuperada = abrir_archivo.read()
                                try:
                                    person_obj_recuperado = pickle.loads(data_serializada_recuperada)
                                except Exception as e:
                                    print(f"Error deserealizar {archivo1}: {e}")
                                    sys.exit(1)

                                person_obj_recuperado.display_info()

                                print("")
                                contador1=2
                            except Exception as e:
                                print("NO se puede imprimir por que no se ha creado el archivo binario ")
                                print("")
                                sys.exit(1)

                        contador1=10
            else:
                print("")
                print('el archivo NO existe')
                print("")                        
                    
        
        else:
            print("")
            print("ingrese un comando valido")
            print("") 
            break 
        break
 
if __name__ == "__main__":
    Menu()