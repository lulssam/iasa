'''
Ações em paralelo: Ações que não interferem entre si e podem ser executadas ao mesmo tempo
Quando não é possivel executar as ações em paralelo, fazemos uma seleção de ações.
A prioridade por hierarquia ocorre quando os comportamentos mais prioritários estão mais altos
na hierarquia.
Associa-se uma prioridade a cada resposta.
Fala-se de seleção de ação por prioridade quando vê se a ação mais alta na hierarquia e associa-se
à ação.

'''

from ecr.comport_comp import ComportComp

class Hierarquia(ComportComp):
    # As ações vêm pela ordem de prioridade dos comportamentos internos sendo a primeira a mais prioritária.
    def selecionar_accao(self, accoes):
        if accoes:
            accao_selecionada = accoes[0]
        
        return accao_selecionada