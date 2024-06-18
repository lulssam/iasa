'''
Mecanismos de raciocinio:
exploração de opções possíveis para encontrar uma solução através de simulação
prospectiva, tendo por base uma representação interna do problema

vs

Mecanismo de procura:



Processo de procura ocorre por exploração do espaço de estados a partir
do estado inicial. O espaço de estados é representado com um garfo, onde
cada vértice corresponde a um estado e cada arco corresponde a uma transição
entre estados.

Procura em profundidade -> estratégia de controlo onde exploramos primeiro os
nós mais recentes fazendo a remoção no inicio da fronteira. Os nós mais 
recentes são inseridos no início da fronteira.
Esta forma de procura aumenta a profundidade do ramo corrente de procura.

Procura em largura -> estratégia de controlo onde ao contrário da anterior,
começamos por explorar os nós mais antigos fazendo a remoção no inicio da 
fronteira e depois os nós mais recentes são inseridos no fim da fronteira.
Nesta procura leva à exploração exaustiva de cada nível de
procura antes da exploração de nós a um nível de maior
profundidade
'''

from abc import ABC, abstractmethod
from pee.mec_proc.no import No
from pee.mec_proc.solucao import Solucao

class MecanismoProcura(ABC):
    # procura geral (profundidade, fronteiras...)
    def __init__(self, fronteira):
        # guardar a fronteira
        self._fronteira = fronteira
        
    
    #construção das estruturas de dados que mantém o código
    def _iniciar_memoria(self):
        # programação incremental
        # 1. iniciar a fronteira -> invocar método iniciar da classe fronteira
        self._fronteira.iniciar()
    
    
    @abstractmethod
    # consoante o mecanismo, a maneira de memorizar é diferente é por isso que fica abstracto
    def _memorizar(self, no):
        raise NotImplementedError
    
    # nucleo deste mecanismo
    def procurar(self, problema):
        ''' inicar a memoria
            criar um nó que corresponde ao estado inicial do problema usando a classe nó
            depois de criar, vamos memorizar o nó
            vamos entrar no ciclo while enquanto a fronteira não estiver vazia (fronteira tem uma propriedade vazia)
            remover o nó da fronteira
            vamos ver se o estado desse nó é o estado desse problema
            se estado do nó for objectivo do problema, retorna uma istnacia solunção com esse nó
        '''
        self._iniciar_memoria()
        no = No(problema.estado_inicial)
        self._memorizar(no) 
        
        while (not self._fronteira.vazia):
            no = self._fronteira.remover()
            if problema.objectivo(no.estado):
                return Solucao(no)
            for no_sucessor in self._expandir(problema, no):
                self._fronteira.inserir(no_sucessor)
                
            
        #raise NotImplementedError
    
    def _expandir(self, problema, no):
        '''
        para cada no sucessor foi gerar por expandir, vamos memorizar esse nó.
        Começamos por iniciar a lista sucessores vazia
        Obtemos o estado do nó
        Para cada operador do problema:
            - geramos estado sucessor aplicando o operadr ao estado atual
            Se o nó sucessor existir:
                - Calcular o custo do nó sucessor que é custo até ao nó antecessor + custo da transição para o estado sucessor)
                - Gerar nó sucessor
                - Juntar nó sucessor à lista de nós sucessores
        No final, retornamos a lista de nós sucessores
        '''
        sucessores = []
        estado = no.estado
        for operador in problema.operadores:
            estado_suc = operador.aplicar(estado)
            if estado_suc is not None:
                custo = no.custo + operador.custo(estado, estado_suc)
                no_sucessor = No(estado_suc, operador, no, custo)
                sucessores.append(no_sucessor)
        return sucessores