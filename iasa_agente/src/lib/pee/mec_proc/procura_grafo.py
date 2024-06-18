from pee.mec_proc.mecanismo_procura import MecanismoProcura

'''
O processo de procura ocorre por exploração do espaço de estados a partie do estado
incial.
O espaço de estados é representado como um garfo, onde cada vértice corresponde
a um estado e cada arco corresposnde a uma transição entre estados.

Em cada passo de processamento:
    * É verificado se o estado actual corresponde ao objectivo
    * Não sendo o estado actual um objectivo, esse estado é expandido
    sendo gerados todos os estados sucessores por aplicação dos vários
    operadores possíveis
    * Para cada estado sucessor, é repetido o processo.
    * Se não existirem estados sucessores, a procura para com a indicação
    de que não existe solução
'''

class ProcuraGarfo(MecanismoProcura):
    '''
    não é abstracto.
    iniciar memoria implica iniciar mais coisas. Vamos programar incremental
    juntamos aquilo que é diferente
    iniciamos dicionario protegido
    '''
    def _iniciar_memoria(self):
        super()._iniciar_memoria()
        self._explorados = {}
        
    '''
    so vamos inserir o no se o estado desse nó ainda não estiver nos explorados para evitar
    nos repetidos
    e se assim for, atualizamos o nó dos explorados.
    
    '''    
    def _memorizar(self, no):
        if (self._manter(no)):
            self._fronteira.append(no)
    
    # boolean
    '''
    indica se nó é para manter ou não
    inclui a condição de manter
    retorna um booleano
    '''
    def _manter(self, no):
        return no.estado not in self._explorados
        
    @property
    def _explorados(self):
        return self._explorados