
import random
import threading
import time
import datetime

PUERTAS=20
THREADS = 2
wantp1=False
wantp2=False
last=1
entradas_1=0
entradas_2=0
entradas_totales=0
tiempo_total_1=0
tiempo_total_2=0

def p1():
    global tiempo_total_1,entradas_1,entradas_2,entradas_totales
    for i in range(PUERTAS//THREADS):
        time.sleep(random.randrange(5))
        wantp1=True
        last=1
        while wantp2 and last==1:
            pass
        #SECCION CRITICA
        t=datetime.datetime.now()
        t_s=t.strftime("%H:%M:%S:%f")
        if i !=0:
            tiempo_total_1 += (t-t_ant).total_seconds()
        entradas_1+=1
        entradas_totales=entradas_1+entradas_2
        print(f"Puerta 1: {entradas_1} entradas de {entradas_totales} Tiempo: {t_s} ")
        
    
        t_ant=t
        wantp1=False


def p2():
    global tiempo_total_2,entradas_1,entradas_2,entradas_totales
    for i in range(PUERTAS//THREADS): 
        time.sleep(random.randrange(5))
        wantp2=True
        last=2
        while wantp1 and last==2:
            pass
        #SECCION CRITICA
        t=datetime.datetime.now()
        t_s=t.strftime("%H:%M:%S:%f")
        if i !=0:
            tiempo_total_2 += (t-t_ant).total_seconds()
        entradas_2+=1
        entradas_totales=entradas_1+entradas_2
        print(f"Puerta 2: {entradas_2} entradas de {entradas_totales} Tiempo: {t_s} ")
        
    
        t_ant=t
    
    wantp2=False



def main():

    t1 = threading.Thread(target = p1)
    t2 = threading.Thread(target = p2)

    print("Entrada 1")
    print("Entrada 2")
    
    t1.start()
    t2.start()

    t1.join()
    t2.join()

    tiempo_medio_1=round(tiempo_total_1/(PUERTAS//THREADS),4)
    tiempo_medio_2=round(tiempo_total_2/(PUERTAS//THREADS),4)

    print(f"Entradas totales: {entradas_totales}")
    print(f"Tiempo medio puerta 1: {tiempo_medio_1}")
    print(f"Tiempo medio puerta 2: {tiempo_medio_2}")
    

if __name__ == "__main__":
    main()