'''
Classe que representa um comportamento composto que corresponde ao objectivo de recolher alvos.
Para recolher alvos precisamos primeiro de aproximar alvos, observar e explorar. Estes são subcomportamentos
que estão organizados em hierarquia.

Niveis de competencia: 3 niveis de competência: aproximar, evitar, explorar, encapsulados de forma
modular através dos respetivos comportamentos.

Tipos de seleção de ação: existe uma hierarquia fixa de prioridade entre comportamentos.

A lista comportamentos tem primeiro ContarPassos pois se estivesse depois do Explorar, não iria gerar a ação.
Metemos em primeira para na hierarquia ficar primeiro e então gerar a ação.

'''

from agente.controlo_react.reações.aproximar.aproximar_alvo import AproximarAlvo
from agente.controlo_react.reações.contar_passos import ContarPassos
from agente.controlo_react.reações.evitar.evitar_obst import EvitarObst
from agente.controlo_react.reações.explorar.explorar import Explorar
from ecr.hierarquia import Hierarquia

class Recolher(Hierarquia):
    def __init__(self):
        comportamentos = [AproximarAlvo(), EvitarObst(), Explorar()]
        # Hierarquia logo metemos no inicio da lista o ContarPassos primeiro para gerar a ação.
        #comportamentos = [AproximarAlvo(), Explorar()]
        super().__init__(comportamentos)