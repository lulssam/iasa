# Implementação do mecanismo base de um comportamento reactivo

from sae import Controlo

class ControloReact(Controlo):
    def __init__(self, comportamento):
        self._comportamento = comportamento
        # Mostrar os sensoriais
        self.mostrar_per_dir = True
        
    def processar(self, percepcao):
        accao = self._comportamento.activar(percepcao)
        return accao

        