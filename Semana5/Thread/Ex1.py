import concurrent.futures
import time
import threading

start = time.perf_counter()

# Forma 1

""" def do_something():
    print(f'Dormindo 1 segundo...')
    time.sleep(1)
    print('Acordou...')

# do_something()
# do_something()
# t1 = threading.Thread(target=do_something)
# t2 = threading.Thread(target=do_something)

# t1.start()
# t2.start()

# t1.join()
# t2.join()

threads = []

for _ in range(10):
    t = threading.Thread(target=do_something)
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()

finish = time.perf_counter()

print(f'Terminou em {round(finish-start, 2)} segundo(s)') """

## Forma 1 com alterações no com um argumento de entrada no do_something


""" def do_something(seconds):
    print(f'Dormindo {seconds} segundo(s)...')
    time.sleep(seconds)
    print('Terminou de Dormir...')

threads = []

for _ in range(10):
    t = threading.Thread(target=do_something, args=[1.5])
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()

finish = time.perf_counter()

print(f'Terminou em {round(finish-start, 2)} segundo(s)') 
 """

## Forma 2

def do_something(segundos):
    print(f'Dormindo {segundos} segundo(s)...')
    time.sleep(segundos)
    #print('Terminou de Dormir...')
    #return 'Terminou de Dormir...'
    return f'Acordou...{segundos}'


with concurrent.futures.ThreadPoolExecutor() as executor:
    # f1 = executor.submit(do_something, 1)
    # f2 = executor.submit(do_something, 1)

    # print(f1.result())
    # print(f2.result())

    """ secs = [5, 4, 3, 2, 1]
    #results = [executor.submit(do_something, 1) for _ in range (10)]
    results = [executor.submit(do_something, sec) for sec in secs]

    for f in concurrent.futures.as_completed(results):
        print(f.result()) """

    seg = [5, 4, 3, 2, 1]
    resultados = executor.map(do_something, seg)

    for result in resultados:
        print(result)

fim = time.perf_counter()

print(f'Terminou em {round(fim-start, 2)} segundo(s)')