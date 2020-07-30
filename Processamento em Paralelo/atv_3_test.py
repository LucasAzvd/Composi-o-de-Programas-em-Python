from bs4 import BeautifulSoup
from functools import reduce

import multiprocessing as mp
import tarfile
import collections

from atv_3 import *


tar = tarfile.open("dados.tar.gz", "r:gz")
# f = tar.extractfile(member) pega o arquivo. veja o getmembers abaixo
with mp.Pool(4) as pool:
    # extrai os arquivos e recebe um dicionário de {cantor: samples+remix+cover}
    resultado_intermed = pool.imap_unordered(extract_and_process,  tar.getmembers())
    final = reduce(merge_function, resultado_intermed)