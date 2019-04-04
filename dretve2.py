import threading
import queue
import urllib.request
import os

NUM_THREADS = 2

def worker(url, result_queue):
    sadrzaj = urllib.request.urlopen(url).read()
    result_queue.put(sadrzaj)


if __name__ == '__main__':
    result_queue = queue.Queue()

    d1 = threading.Thread(target=worker,
                         args=("http://www.google.com", result_queue))

    d2 = threading.Thread(target=worker,
                          args=("http://www.bing.com", result_queue))

    d2.start()
    d1.start()

    sadrzaj = result_queue.get()
    print(sadrzaj)

    with open("stranica.html", "w") as f:
        f.write(str(sadrzaj))

    os.system("stranica.html")




