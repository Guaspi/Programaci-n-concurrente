import threading

THREADS = 2
MAX_COUNT = 100
turn = 1
n = 0

def p():
    global n, turn
    for i in range(int(MAX_COUNT/THREADS)):
        while turn !=1:
            pass
        n += 1
        turn = 2

def q():
    global n, turn
    for i in range(int(MAX_COUNT/THREADS)):
        while turn != 2 :
            pass
        n += 1
        turn = 1  



def main():
    threads = []

    t1 = threading.Thread(target = p)
    t2 = threading.Thread(target = q)

    
    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Valor de n: ",  n)


if __name__ == "__main__":
    main()