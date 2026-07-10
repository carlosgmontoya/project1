class Statistics:
    def __init__(self, lista):
        self._lista = lista
        #self._multiplicador = multiplicador
        #self._sumando = sumando
    
    def suma(self):
        suma1 = sum(self._lista)
        return suma1

    def canti(self):
        canti1 = len(self._lista)
        return canti1 
    
    def prome(self):
        prome1 =  sum(self._lista) / len(self._lista) 
        return prome1
    
class Graphics:
    pass


