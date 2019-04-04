from multiprocessing import Pool
import time
import sys


def suma_kvadrata(interval):
    a, b = interval
    return sum(i**2 for i in range(a, b+1))


if __name__ == "__main__":
    N = int(sys.argv[1])
    K = int(sys.argv[2])
    start = time.time()
    #print(suma_kvadrata((1, N)))
    intervali = [(1, N//4), (N//4+1, N//2), (N//2+1, 3*N//4), (3*N//4+1, N)]

    with Pool(K) as p:
        rezultati = p.map(suma_kvadrata, intervali)
    print(sum(rezultati))
    end = time.time()
    print("{} sec".format(end-start))