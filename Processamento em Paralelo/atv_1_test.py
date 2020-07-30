import glob

from atv_1 import *

resultadomap = list(map(conta_um_arquivo, glob.glob(pasta)))
next(iter(resultadomap[0].items()))
# ('\ufeffthe', 1)