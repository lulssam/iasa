from deposito.transferir import Transferir
from mod.estado import Estado

class Encher(Transferir):

    # retorna novo estado 
    def aplicar(self, estado):
        return estado.volume + estado.volume