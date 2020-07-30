import threading 

class Factorizador(threading.Thread):
    def __init__(self, num, **kwargs):
        super(Factorizador, self).__init__(**kwargs)
        self.__num = num
        self.__results = None

    def run(self):
        self.__results = []
        for i in range(1, self.__num):
            if self.__num % i == 0:
                self.__results.append(i)

    def get_results(self):
        return [i for i in self.__results]

def main():
    f1 = Factorizador(12312387)
    f2 = Factorizador(1231532)
    f1.start()
    f2.start()
    f1.join()
    f2.join()
    print(f1.get_results())
    print(f2.get_results())

main() # slide 71
