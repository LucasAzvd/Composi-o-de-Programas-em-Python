from atv_1 import Ponto2D, Retangulo

r1_esq_sup = Ponto2D(-6.5, 5.0)
r1_dir_inf = Ponto2D(-2.0, 2.5)
ret1 = Retangulo(r1_esq_sup, r1_dir_inf)

area1 = ret1.calcularArea() 
print("%.2f %.2f %.2f" % (ret1.width, ret1.height, area1))

r2_esq_sup = Ponto2D(2.0, 7.0)
r2_dir_inf = Ponto2D(5.0, 4.0)
ret2 = Retangulo(r2_esq_sup, r2_dir_inf)
area2 = ret2.calcularArea()
print("%.2f %.2f %.2f" % (ret2.width, ret2.height, area2))

intersecao = ret1.calcularIntersecao(ret2)
print(intersecao)

"""
Saída esperada:

 4.50 2.50 11.25
 3.00 3.00 9.00 
 None
"""

from atv_1 import Ponto2D, Retangulo

r1_esq_sup = Ponto2D(-6.5, 5.0)
r1_dir_inf = Ponto2D(-2.0, 2.5)
ret1 = Retangulo(r1_esq_sup, r1_dir_inf)

r2_esq_sup = Ponto2D(-4.5, 4.0)
r2_dir_inf = Ponto2D(-1.0, 1.5)
ret2 = Retangulo(r2_esq_sup, r2_dir_inf)

intersecao = ret1.calcularIntersecao(ret2)
print(intersecao)
""" 3.5 """

r1_esq_sup = Ponto2D(-7.0, 1.0)

r1_dir_inf = Ponto2D(7.0, -3.0)
ret1 = Retangulo(r1_esq_sup, r1_dir_inf)
r2_esq_sup = Ponto2D(3.0, 3.0)
r2_dir_inf = Ponto2D(6.0, -2.0)
ret2 = Retangulo(r2_esq_sup, r2_dir_inf)

intersecao = ret1.calcularIntersecao(ret2)
print(intersecao)
""" 9 """