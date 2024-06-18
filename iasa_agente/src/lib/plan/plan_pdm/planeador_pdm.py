from pdm.pdm import PDM
from plan.modelo.modelo_pdm_plan import ModeloPDMPlan
from plan.plan_pdm.plano_pdm import PlanoPDM
from plan.planeador import Planeador


class PlaneadorPDM(Planeador):
    def __init__(self, gama = 0.85, delta_max = 1):
        self.__gama = gama
        self.__deltamax = delta_max
        
    def planear(self, modelo_plan, objetivos):
        # se houverem objetivos
        if objetivos:
            # invocar classe ModeloPDMPlan
            modelo_pdm = ModeloPDMPlan(modelo_plan, objetivos)
            pdm = PDM(modelo_pdm, self.__gama, self.__deltamax)
            # resolver com utilidade e politica
            utilidade, politica = pdm.resolver()
            return PlanoPDM(utilidade, politica)
        # else:
        #     return None