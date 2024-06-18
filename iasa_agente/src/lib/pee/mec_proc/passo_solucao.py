from dataclasses import dataclass
from lib.mod.estado import Estado
from lib.mod.operador import Operador

'''
Dataclasses facilitam o desenvolvimento do código
'''
@dataclass
class PassoSolucao:
        estado: Estado
        operador: Operador