
from agente.controlo_delib.controlo_delib import ControloDelib
from plan.plan_pdm.planeador_pdm import PlaneadorPDM
from sae.agente.agente import Agente

'''
Modulo para iniciar Agente Delib PDM
Estende classe 
'''

class AgenteDelibPDM(Agente):
    def __init__(self):
        planedor = PlaneadorPDM()
        controlo = ControloDelib(planedor)
        super().__init__(controlo)