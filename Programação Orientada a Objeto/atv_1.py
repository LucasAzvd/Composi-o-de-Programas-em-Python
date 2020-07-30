class Ponto2D:
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y

class Retangulo:
    def __init__(self, __esq_sup, __dir_inf):
        self.__esq_sup = __esq_sup
        self.__dir_inf = __dir_inf
    
    @property
    def esq_sup(self):
        return self.__esq_sup

    @property
    def dir_inf(self):
        return self.__dir_inf

    @property
    def width (self):
        return (self.__dir_inf.x - self.__esq_sup.x)

    @property
    def height(self):
        return  (self.__esq_sup.y - self.__dir_inf.y)

    def calcularArea(self):
        lado1 = self.__esq_sup.y - self.__dir_inf.y
        lado2 = self.__dir_inf.x - self.__esq_sup.x 
        return lado1*lado2

    def calcularIntersecao(self,ret):
        if(self.__dir_inf.x < ret.esq_sup.x or self.__dir_inf.y > ret.esq_sup.y):
            return None
        elif (ret.esq_sup.x > self.__esq_sup.x and ret.dir_inf.y > self.__dir_inf.y):
            lado1 = ret.esq_sup.x - ret.dir_inf.x
            lado2 = ret.dir_inf.y - self.__esq_sup.y
            return abs(lado1*lado2)
        else:
            lado1 = ret.esq_sup.x - self.__dir_inf.x
            lado2 = ret.esq_sup.y - self.__dir_inf.y
            return abs(lado1*lado2)
