import threading

class MinhaThread(threading.Thread):
    def __init__(self, contador, **kwargs):
        super(MinhaThread, self).__init__(**kwargs)
        self.__cnt = contador

    def run(self):
        print(self.__cnt.add_and_get())

class Contador(object):
    def __init__(self):
        self.__value = 0

    def add_and_get(self):
        self.__value += 1
        return self.__value

def main():
    cnt = Contador()
    threads = []
    for i in range(100): threads.append(MinhaThread(cnt))
    for i in range(100): threads[i].start()
    for i in range(100): threads[i].join()

if __name__ == '__main__':
    main()