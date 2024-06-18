# Interface que define a funcionalidade geral de um estímulo (concretixado em função do problema a resolver)

from abc import ABC, abstractmethod

# Classe abstracta
class Estimulo(ABC):
    @abstractmethod # anotação
    def detectar(self, percepcao):
        """...""" # string tripla


