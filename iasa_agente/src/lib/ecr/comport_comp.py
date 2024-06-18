# Implementação do mecanismo base de um comportamento composto.

from abc import ABC, abstractmethod

# Classe abstracta
class ComportComp():
    # Construtor
    @abstractmethod
    def __init__(self, comportamentos):
        self.__comportamentos = comportamentos

    def activar(self, percepcao):
        accoes = [] # lista para ações
        for comportamento in self.__comportamentos: # para cada comportamento
            accao = comportamento.activar(percepcao) # activar 
            if accao: # se ação existir
                accoes.append(accao) # adicionar à lista
        
        # se a lista existir, selecionamos uma ação
        if accoes:
            return self.selecionar_accao(accoes)
                

    @abstractmethod
    def selecionar_accao(self, accoes):
        """..."""