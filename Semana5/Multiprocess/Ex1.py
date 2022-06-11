import time
import multiprocessing
import concurrent.futures

start = time.perf_counter()

## FORMA 1

""" def do_something():
    print('Dormindo 1 segundo...')
    time.sleep(1)
    print('Acordou...')


# do_something()
# do_something()


def multriprocessF():
    p1 = multiprocessing.Process(target=do_something)
    p2 = multiprocessing.Process(target=do_something)

    p1.start()
    p2.start()

    p1.join()
    p2.join()

if __name__ == '__main__':
    multriprocessF() """

## FORMA 2

""" def do_something(seconds):
    print(f'Dormindo {seconds} segundo(s)...')
    time.sleep(seconds)
    print('Acordou...')

processes = []

def multriprocessF():
    for _ in range(10):
        p =  multiprocessing.Process(target=do_something, args=[1.5])
        p.start()
        processes.append(p)

    for process in processes:
        process.join()

    finish = time.perf_counter()

    print(f'Terminou em {round(finish-start, 2)} segundo(s)') 

if __name__ == '__main__':
    multriprocessF()
 """

## FORMA 3

def tempo(segundos):
    print(f'Dormindo {segundos} secondo(s)...')
    time.sleep(segundos)
    return f'Acordou...{segundos}'

def multriprocessF():
    with concurrent.futures.ProcessPoolExecutor() as executor:
        # f1 = executor.submit(tempo, 1)
        # f2 = executor.submit(tempo, 1)

        # print(f1.result())
        # print(f2.result())
        seg = [ 4, 3, 2, 1]
        resultados = executor.map(tempo, seg)

        for result in resultados:
            print(result)

    fim = time.perf_counter()

    print(f'Terminou em {round(fim-start, 2)} segundo(s)')

if __name__ == '__main__':
    multriprocessF()