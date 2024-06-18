# Imports
from agente.controlo_delib.mec_delib import MecDelib
from agente.controlo_delib.modelo.modelo_mundo import ModeloMundo
from sae.agente.controlo import Controlo

'''
Clase responsavel por controlar o comportamento de um agente deliberativo.
Implementa interface Controlo do SAE.
'''

class ControloDelib(Controlo):
    # Construtor da classe
    def __init__(self, planeador):
        self.__planeador = planeador
        self.__modelo_mundo = ModeloMundo()
        self.__mec_delib = MecDelib(self.__modelo_mundo)
        self.__plano = None
        # lista de objetivos iniciada a none
        self.__objetivos = None
        #super().__init__()
        
    # Passo da tomada de decisão
    def processar(self, percepcao):
        self.__assimilar(percepcao)
        if self.__reconsiderar():
            self.__deliberar()
            self.__planear()
            
        acao = self.__executar()
        self.__mostrar()
        return acao
        
    # Atualizar o modelo do mundo
    def __assimilar(self, percepcao):
        self.__modelo_mundo.actualizar(percepcao)
        
    
    # Agente vai reconsiderar se não houver plano ou o modelo do mundo estiver sido alterado
    def __reconsiderar(self):
        # if not self.__plano or self.__modelo_mundo.__alterado():
        #     self.__plano.reconsiderar()
        # CORRIGIDO
        return not self.__plano or self.__modelo_mundo.alterado
        

    # Ativar o planeador. Planeador tem método planear
    # Atribuir ao plano o resultado deste planear. 
    # Retorna um plano.
    def __planear(self):
        self.__plano = self.__planeador.planear(self.__modelo_mundo, self.__objetivos)
    
    # Atualiza os objetivos do agente. Ojetivos são gerados no método deliberar. 
    # Ativa o deliberar do mecanismo deliberativo
    def __deliberar(self):
        # objetivo = self.__mec_delib.deliberar()
        # self.__objetivos.append(objetivo)
        self.__plano = self.__planeador.planear(self.__modelo_mundo, self.__objetivos)
        
    # retorna a mesma ação do que o processar.
    # Se existir plano, vai executar a ação corrente do plano. O plano, tem o méotodo obter_acao().
    # Verficar se há plano. Caso true -> Sobre o plano, obter acao do estado atual do agente que está 
    # no modelo do mundo usando o obter estado. No Operador, obter a ação que retorna um operador mover.
    # Caso false -> Não retorna nada.
    def __executar(self):
        # Verificar se há plano
        # if self.__plano:
        #     # Se houver plano
        #     operador = self.__plano.obterAccao(self.__modelo_mundo.obter_estado())
        #     return operador
        # else:
        #     return None
        
        # codigo mais completo
        # se houver plano
        if self.__plano:
            # obter estado pelo modelo mundo
            # estado = self.__modelo_mundo.obter_estado()
            # obter operador pleo plano
            operador = self.__plano.obter_accao(self.__modelo_mundo.obter_estado())
            # se houver operador
            if operador:
                # retornar a accao
                return operador.accao
            # caso contrário
            else:
                # plano é none            
                self.__plano = None
        
    # mostar o modelo do mundo. Usando o vista do SAE
    def __mostrar(self):
        # vista = Controlo.vista()
        # self.__modelo_mundo.mostrar(vista)
        # self.__planear.mostrar(vista)
        
        # codigo mais completo
        self.vista.limpar()
        self.__modelo_mundo.mostrar(self.vista)
        if self.__plano:
            self.__plano.mostrar(self.vista)
        if self.__objetivos:
            for objetivo in self.__objetivos:
                self.vista.marcar_posicao(objetivo.posicao)