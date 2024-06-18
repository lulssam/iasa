from deposito.transferir import Transferir


class Vazar(Transferir):
    '''diminui ao longo do estado o seu proprio volume'''
    def aplicar(self, estado):
        volume = self.volume = estado.volume
        return 0 if volume < 0 else volume