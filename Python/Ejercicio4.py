import random
import threading
import time



CONTADOR=20
THREADS = 2
wantp=0
wantq=0


def p():
    global wantp,wantq
    for i in range(CONTADOR//THREADS):
        if wantq==-1:
            wantp=-1
        else:
            wantp=1
        
        while wantq==wantp:
            pass

        #SECCION CRITICA
        print("proceso A entra en la seccion critica")
        time.sleep(random.randrange(5))
        print("proceso A sale de la seccion critica")


        wantp=0

def q():
    for i in range(CONTADOR//THREADS):
        if wantp==-1:
            wantq=1
        else:
            wantq=-1
        
        while wantp==-wantp:
            pass

            #SECCION CRITICA
        print("proceso B entra en la seccion critica")
        time.sleep(random.randrange(5))
        print("proceso B sale de la seccion critica")
        wantq=0


def main():
    
    t1 = threading.Thread(target = p)
    t2 = threading.Thread(target = q)

    t1.start()
    t2.start()

    t1.join()
    t2.join()




if __name__ == "__main__":
    main()