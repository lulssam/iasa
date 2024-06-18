'''

Classe que trata de atribuir a ação ao agente. Controlo Reativo em que o processar
das precepções é realizado com base num módulo comportamental, também designado comportamento,
o qual representa o comportamento geral do agente que pode ser constituido por diferenetes
sub-comportamentos.

'''




from agente.controlo_react.controlo_react import ControloReact
from agente.controlo_react.reações.recolher import Recolher
from sae.agente.agente import Agente


class AgenteReactivo(Agente):
    def __init__(self):
        #comportamento = ContarPassos()
        comportamento = Recolher()
        #comportamento = Explorar()
        controlo = ControloReact(comportamento)
        super().__init__(controlo)
    
    
# criar uma instância da classe ControloReact, 
# aqui definimos que o controlo do agente é baseado nas reações do comportamento