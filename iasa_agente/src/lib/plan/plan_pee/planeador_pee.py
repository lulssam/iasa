''' requer modelo de planeamento'''
from pee.melhor_primeiro.procura_aa import ProcuraAA
from plan.plan_pee.mod_prob.heur_dist import HeurDist
from plan.plan_pee.mod_prob.prob_plan import ProblemaPlan
from plan.plan_pee.plano_pee import PlanoPEE
from plan.planeador import Planeador


class PlaneadorPEE(Planeador):
    # construtor
    def __init__(self):
        self.__mec_pee = ProcuraAA()  
       
    def planear(self, modelo_plan, objetivos):
        # se houver objetivos
        if objetivos:
            # estado final vai ser o primeiro objetivo da lista de objetivos
            estado_final = objetivos[0]
            # criamos um problema
            problema = ProblemaPlan(modelo_plan, estado_final)
            # definir heuristica com estado final
            heuristica = HeurDist(estado_final)
            solucao = self.__mec_pee.procurar(problema, heuristica)
        # se houver solução    
        if solucao:
            return PlanoPEE(solucao)