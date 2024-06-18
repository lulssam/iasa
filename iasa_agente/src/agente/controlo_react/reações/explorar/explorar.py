'''
Comportamento simples fixo.
Quando for ativado, vai fazer uma movimentar numa diração aleatória

Não depende de estimulo, está sempre a gerar respostas.
Usamos o choice para fazer uma escolha aleatória da direção
'''
from random import choice
from agente.controlo_react.reações.resposta.resposta_mover import RespostaMover
from sae import Direccao
from ecr.comportamento import Comportamento


class Explorar(Comportamento):
   
    def direcao_aleatoria(self):
        direcoes = list(Direccao)
        return choice(direcoes)
    
    def activar(self, percepcao): # retorna ativação da resposta
        direcao = Explorar.direcao_aleatoria(self)
        resposta = RespostaMover(direcao)
        return resposta.activar(percepcao)