import threading
import time
from queue import Queue


def job(I, q):
    for i in range(len(I)):
        I[i] = I[i] ** 2
    q.put(I)


def multithreading(data):
    q = Queue()
    threads = []
    for i in range(4):
        t = threading.Thread(target=job, args=(data[i], q))
        t.start()
        threads.append(t)
    for thread in threads:
        thread.join()
    results = []
    for _ in range(4):
        results.append(q.get())
    print(results)


if __name__ == '__main__':
    data = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
    multithreading(data)
