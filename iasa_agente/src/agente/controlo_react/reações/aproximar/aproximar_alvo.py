'''
Sub-comportamento Aproximar alvo

Este sub-comportamento faz com que o agente tenha capacidade de percepcinar e de avançar 
em 4 direções (Norte, Sul, Este e Oeste).

Seleção de ação: Para a coordenação de sub-comportamentos depende das características dos 
sub-comportamentos e do objectivo do comportamento composto que os agrega.
'''

from agente.controlo_react.reações.aproximar.aproximar_dir import AproximarDir
from ecr.prioridade import Prioridade
from sae.ambiente.direccao import Direccao

class AproximarAlvo(Prioridade):
    def __init__(self):
        # comportamentos = [AproximarDir(Direccao.NORTE), AproximarDir(Direccao.SUL), AproximarDir(Direccao.ESTE), AproximarDir(Direccao.OESTE)]
        # super()._init_(comportamentos)
        
        # Alteração para ter código menos redundante
        comportamentos = [AproximarDir(direccao) for direccao in Direccao]
        super().__init__(comportamentos)