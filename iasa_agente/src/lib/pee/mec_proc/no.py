'''
Classe que vai representar os nós com os seus estados,
operador, profundindade e custo.
'''

class No():
    
    '''
    Não se pode ter dois contrutores então em python
    Duas formas do construtor vão fundir numa só. Os parametros comuns são obrigatorios.
    Os que só existem num vão ter valores por omissão
    se houver antecedor -> profundidade = antecedor + 1
    '''
    def __init__(self, estado, operador = None, antecedor = None, custo = 0):
        self.__estado = estado
        self.__operador = operador
        self.__antecedor = antecedor
        self.__custo = custo
    
    @property
    def estado(self):
        return self.__estado
    
    @property
    def operador(self):
        return self.__operador
    
    @property
    def profundidade(self):
        if self.__antecedor():
            self._profundidade = self.__antecedor.profundidade() +1
            return self._profundidade
        return 0
    
    @property
    def custo(self):
        return self.__custo