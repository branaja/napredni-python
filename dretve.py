import threading
import queue

NUM_THREADS = 4


def worker(work_queue, result_queue):
    while True:
        item = work_queue.get()
        if item == 'END':
            break
        result_queue.put(item ** 2)
        #print(item ** 2)
        work_queue.task_done()


if __name__ == '__main__':
    work_queue = queue.Queue()
    result_queue = queue.Queue()

    threads = [
        threading.Thread(target=worker,
                         args=(work_queue, result_queue))
        for i in range(NUM_THREADS)
    ]

    for thread in threads:
        thread.start()

    for i in range(1, 11):
        work_queue.put(i)

    work_queue.join()
    print('all items processed')

    for i in range(0, NUM_THREADS):
        work_queue.put("END")

    while threads:
        threads.pop().join()

    while not result_queue.empty():
        print(result_queue.get())
