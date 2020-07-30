import threading
import urllib.request
import concurrent.futures
import os

class Worker(threading.Thread):
    def __init__(self, _id):
        self._id = _id
        self.num_linha = 0

    def run(self):
        try:
            response = urllib.request.urlopen('http://www.gutenberg.org/files/{}/{}-0.txt'.format(self._id, self._id))
            response = response.read().decode('utf-8')
            response = response.split('\n')        
            self.num_linha = len(response) - 1
        except:
            self.num_linha = 0

    def get_result(self):
        return self.num_linha


def crawler(num_threads):
    pasta =  os.path.join('.', 'dados', 'ids.txt')
    data = []
    with open(pasta, 'rb') as input_file:
        for line in input_file:
            line = line.strip()
            line = int(line)
            data.append(line)
    total = 0
    with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as executor:
        # O with funciona como um .join()
        for resultado in executor.map(Worker, data):
            resultado.run()
            total+=resultado.get_result()
    return total + 1
