# -*- coding: utf8

from bs4 import BeautifulSoup
from functools import reduce

import multiprocessing as mp
import tarfile
import collections

def extract_and_process(member):
    # observe como cada processo abre o tar novamente
    # a extração é feita por processo
    # veja exemplos do HTML na pasta exemplo
    # Para pegar o nome de um artist use texto.strip().split('-')[-1].
    # O formato do texto no html é Música - Artista
    tar = tarfile.open("dados.tar.gz", "r:gz")
    f = tar.extractfile(member)
    soup = BeautifulSoup(f, 'html.parser')
    json_response = {}
    for response in soup.find_all(class_='trackInfo'):
        artista = response.find(class_='trackName').string.strip().split('- ')[-1]
        reproducoes = int(response.find(class_='counts').string.strip().split(' ')[1])
        if artista in json_response.keys():
            reproducoes_atual = json_response[artista]
            json_response[artista] = reproducoes_atual + reproducoes
        else:
            json_response[artista] = reproducoes
    return collections.Counter(json_response)

def merge_function(dict_1, dict_2):
    return dict_1 + dict_2

def mapreduce(num_cpus=2):
    tar = tarfile.open('dados.tar.gz', 'r:gz')
    if num_cpus > 1:
        with mp.Pool(num_cpus) as pool:
            intermed = pool.imap_unordered(extract_and_process,
                                           tar.getmembers())
    else:
        intermed = map(extract_and_process, tar.getmembers())
    final = reduce(merge_function, intermed)
    return final