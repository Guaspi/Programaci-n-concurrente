#Carlos Guasp López| Práctica 1: Juzgado

from asyncio import sleep
import random
import threading
import time


nombres = ["Deadshot","Harley Quinn","Penguin","Riddler","Bane","Talia al Ghul","Ra's al Ghul","Hugo Strange","Killer Croc", "Catwoman",
           "Poison Ivy","Mr. Freeze","Jason Todd","Hush","Joker","Deathstroke","Mad Hatter","Two-Face","Scarecrow","Clayface"]

NUM_SOSPECHOSOS=20
contador_sospechosos=0 
contador_fichados=0
contador_declaraciones=0
sala_entrada=threading.Semaphore(1) #declarado a 1 ya que quiero que nada más llegar un sospechoso pueda entrar.
sala_declarar=threading.Semaphore(0)  #declarado a 0 ya que espero a que el juez de la indicacion de declarar.
sala_entrada_asil=threading.Semaphore(0)  #declarado a 0 ya que espero a que el juez de la indicacion de ir al asilo
fichados=threading.Semaphore(1)  #declarado a 1 ya que quiero que nada más puedan fichar, fichen.
abandona_juez=False


class Juez(threading.Thread):  
   

    def __init__(self):
        super(Juez,self).__init__()

    def run(self):
        global contador_sospechosos,contador_fichados,contador_declaraciones,abandona_juez
        
        #AQUI SE PUEDE AÑADIR ESPERA
        print("----> Jutge Dredd: Jo som la llei!")  
        sala_entrada.acquire()
        #AQUI SE PUEDE AÑADIR ESPERA
        print("----> Jutge Dredd: Som a la sala, tanqueu porta!")
        
        if contador_sospechosos>=1:  #si hay algun sospechoso el juez actuará en consecuencia.
            print("----> Jutge Dredd: Fitxeu als sospitosos presents")
      
            while contador_fichados<contador_sospechosos:
                pass
            print("----> Jutge Dredd: Preniu declaració als presents")
            sala_declarar.release()

            while contador_declaraciones<contador_fichados:
                pass
            print("----> Judge Dredd: Podeu abandonar la sala tots a l'asil!")
            sala_entrada_asil.release()
        else:       # si no hay ninún sospechoso, el juez se irá sin preguntar.
            print("----> Jutge Dredd: Si no hi ha ningú me'n vaig!")

          #AQUI SE PUEDE AÑADIR ESPERA
        print("----> Jutge Dredd: La justícia descansa, prendré declaració als sospitosos que queden")

        abandona_juez=True   #variable para saber si el juez ha abandonado o no. Así sabremos como debe actuar el sospechoso.
        sala_entrada.release()
  

class Sospechoso(threading.Thread):
    
    def __init__(self,nombre):
        super(Sospechoso,self).__init__()
        self.__nombre=nombre

    def run(self):
        global contador_sospechosos,contador_fichados,contador_declaraciones #variables para ir sumando cada apartado.

        
        print(f"{self.__nombre}: Som inocent!")
        time.sleep(1)
        sala_entrada.acquire() #semáforo sala entrada
        if not abandona_juez:  #si el juez no ha abandonado la sala, entra.

            #AQUI SE PUEDE AÑADIR ESPERA
            contador_sospechosos+=1
            print(f"{self.__nombre} entra al jutjat. Sospitosos: {contador_sospechosos}")
            sala_entrada.release()
            
            fichados.acquire() #semáforo para fichar
              #AQUI SE PUEDE AÑADIR ESPERA
            contador_fichados+=1
            print(f"{self.__nombre} fitxa. Fitxats: {contador_fichados}")
            fichados.release()
        

            sala_declarar.acquire() #semaforo para declarar
             #AQUI SE PUEDE AÑADIR ESPERA
            contador_declaraciones+=1
            print(f"{self.__nombre} declara. Declaracions: {contador_declaraciones}")
            sala_declarar.release()
            
            sala_entrada_asil.acquire() #semáforo para la entrada al asilo. Esperará la orden del juez.
              #AQUI SE PUEDE AÑADIR ESPERA
            print(f"{self.__nombre} entra a l'Asil d'Arkham")
            sala_entrada_asil.release()
        
        else: #Si no ha podido entrar en la sala despúes del veredicto del juez, acaba.
            print(f"{self.__nombre}: No és just vull declarar! Som innocent!")
            sala_entrada.release()


def main():
    

    threads=[]

    for i in range(NUM_SOSPECHOSOS): #bucle para añadir a threads todos los sospechosos por su nombre.
        threads.append(Sospechoso(nombres[i]))
    threads.append(Juez())     #añado por separado al juez ya que no está en el array "nombres".

    for i in range(len(threads)): #bucle para el .start de todos los hilos.
        threads[i].start()

    for i in range(len(threads)): #bucle para el .join de todos los hilos
        threads[i].join()



if __name__ == "__main__":
    main()