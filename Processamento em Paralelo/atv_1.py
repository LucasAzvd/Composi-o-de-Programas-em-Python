from collections import Counter
from functools import reduce

import glob
import os


def conta_um_arquivo(fpath):
    lista_palavras = []
    with open(fpath, encoding="utf8") as input_file:
        for line in input_file:
            line = line.lower().strip()
            if line:
                palavras = line.split()
                for i in palavras:
                    lista_palavras.append(i)
    return Counter(lista_palavras)

def reduz(contagens_1, contagens_2):
    return contagens_1 + contagens_2

def main():
    pasta =  os.path.join('.', 'dados', '*.txt')
    resultado = reduce(reduz, map(conta_um_arquivo, glob.glob(pasta)))
    return resultado
    
if __name__ == '__main__':
    main()