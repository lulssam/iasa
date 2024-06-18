from agente.controlo_delib.controlo_delib import ControloDelib
from plan.plan_pee.planeador_pee import PlaneadorPEE
from sae.agente.agente import Agente

# Estende classe Agente
class AgenteDelibPEE(Agente):
    # construtor
    def __init__(self):
        planeador = PlaneadorPEE()
        controlo = ControloDelib(planeador)
        # chamar super classe
        super().__init__(controlo)