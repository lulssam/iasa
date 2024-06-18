from mod.estado import Estado

'''
só tem que guardar o valor

tem que ter atributo contagem
convém que seja privado mas tenhamos acesso só para leitura

implementar id_valor

o valor do estado é um inteiro

id valor retorna algo que identifique o nosso estado a partir do valor
logo só precisa de retornar o proprio valor


'''

class EstadoContagem(Estado):
    def __init__(self, valor):
        self._valor = valor
        
    def id_valor(self):
        return self._valor