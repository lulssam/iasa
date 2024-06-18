'''
As respostas são seleccionadas de acordo com uma prioridade associada que varia ao longo da
execução. A primeira ação é a mais prioritária.

'''

from ecr.comport_comp import ComportComp

class Prioridade(ComportComp):
    # As ações vêm pela ordem de prioridade dos comportamentos internos sendo a primeira a mais prioritária.
    def selecionar_accao(self, accoes):
        if accoes:
            funcao_seleccao = lambda accao: accao.prioridade # lambda usado para simplificar função
            accao_selecionada = max(accoes, key=funcao_seleccao)
            return accao_selecionada


'''

from ecr.comport_comp import ComportComp #import da classe ComportComp


Para cada ação nós iremos ter uma prioridade e é através desta 
prioridade que as ações são seleccionadas.
A prioridade de cada ação pode mudar dinamicamente durante 
a execução do programa
Num sistema de processamento de eventos é selecionada primeiro a
resposta com maior prioridade


class Prioridade(ComportComp):

    
      Se houverem ações disponíveis, teremos de retorna a ação com a maior prioridade de entre as ações disponíveis,
      teremos de extrai a prioridade de cada ação
    
    def selecionar_accao(self, accoes):
      
      if accoes:
         #função definida inline, onde temos a palavra chave lamba,
         #realizamos a transformação para retornar a prioridade de cada ação
         funcao_seleccao = lambda accao: accao.prioridade

         #função que retorna o maior valor, key é a função de avaliação para verificar a prioridade da ação
         accao = max(accoes, key=funcao_seleccao) 
         return accao

'''