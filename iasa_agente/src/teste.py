'''
Aula 18 de Março

Arquitectura de agentes reactivos:
O comportamento do sistema é gerado de forma reativa, com base em associações entre estímulos
e respostas.
Os objetivos são implícitos.
Existe um acoplamento forte com o ambiente.
Usamos os veículos de braitenberg como exemplo.

Agentes Reactivos:
Uma arquitectura de agentes reactivos define um ciclo percepção-reação-ação, onde as reações
definem de forma modular as associções entre estímulos e repostas.
No caso de reações simples, as associações estímulo-resposta podem ser definidads através
de regras "SE-ENTÃO".
No caso geral, as reações podem envolver processamento mais complexo, incluindo a manutenção de estado
interno com base em mecanismos de memória. Nessa situação, os vários elementos envolvidos numa 
reação devem ser modularizados, de forma a poderem ser organizados de forma versátil e a 
encapsular a complexidade necessária à sua função.
Devem, então, ser definidos os seguintes elementos:
    - Estimulo -> define informação ativadora de uma reação.
    - Resposta -> define uma resposta a estímulos, termos de ação a realizar e da respectiva
                  prioridade.
    - Reação -> módulo que associa estímulos a respostas.
      
    
Mecanismo de Reação:
Agente reativo -> composto por conjuntos de reações que organizadas são chamadas de comportamentos.
Comportamento -> conjunto de reações relacionadas entre si no sentido de produzirem um resultado especifico.
                 Realiza de forma modular e coesa o encapsulamento das reações internas.
                
Há dois tipos de comportamento:
    - reação = Comportamento simples. Representa uma associação Estímulo-Resposta.
    - comportamento Composto = um comportamento com outro comportamento lá dentro. Requer
                               um mecanismo de seleção de ação para determinar a ação a realizar
                               em função das respostas dos vários comportamentos internos.
              
              
Esquemas Comportamentais Reactivos:
    - Comportamento:
        - Reação
            * Estimulo -> representa a deteção de um estímulo presente numa percepção.
            * Resposta -> representa a geração de uma resposta a um estímulo.

Biblioteca ECR -> agrega estes elementos de forma modular.                  

-----------
nomes das classes em minusculas, nomes dos modulos, metodos, funcoes, packages em minusculas palavras separadas
por_ (excessão: CONSTANTES)
visibilidade: por convenção:
privado: __ antes do nome
protected: _antes do nome
publico: sem nada antes do nome
interfaces:

variaveis iniciadas no construtor. Uma função torna-se num método, se no primeiro argumento receber a classe
respectiva.

na classe uml o construtor tem o mesmo nome da classe, em python passa a ser __init__

qualquer função, para ser método de uma classe tem que te rum argumento self.

não se escreve tipos em python

self pode ser escrito de varias formas, só temos que garantir que é o primeiro argumento.

em métodos que não foram implementados -> raise NotImplemented

string tripla -> anotação para documentação em python

no uml, se tiverem em italico, são abstractos

set PYTHONPATH=src;src/lib

-----------

class A:
    # Construtor
    def __init__(self): # sem argumentos
        self.a1 = None  # ausencia de valor

    def m1(self, p1): # com argumentos
        print(p1)

a = A()
a.m1("teste")

# também corre desta forma:
A.m1(a, "teste") # primeiro argumento tem que ser da sua instância.

##############################################################################################################################################################################################
Aula 25 de Março

Há varios tipos de comportamentos:
    - Comportamento fixo: gera uma ação em permanência. Tem uma reposta fixa (Explorar)
    - Reação: Associa Estºimulo e Resposta.
    - Comportamento composto: Agrega sub-comportamentos (Recolher)

##############################################################################################################################################################################################
Aula 15 de Abril

Resolução automatica de problemas
Problema de puzzle de peças deslizantes:
    Sequência de movimentos

Raciocinio automatico: capacidade de um sistema computacional resolver de forma automatica um
problema com base numa representação de conhecimento do respetico domínio, produzindo uma solução
a partir de diversas alternativas.

É um processo computacional que tendo como entrada uma representação de conhecimento de um determinado
domínio, produz como resultado conclusões baseadas nesse conhecimento

O processo de racicínio automático envolve dois tipos de atividades principais, a exploração
de opções possíveis e a avalição de opções para decisão acerca das melhores opções.

- Exploração de opções:
    * raciocinio prospectivo -> antecipação do que pode acontecer
    * simulação interna do dominio do problema -> requer formas de representação interna do dominio do problema
- Avaliação de opçoes
    * custo -> recursos necessários
    * valor -> ganho ou perda, medido por exemplo em termos de utilidade.


operador gera transição de estado. 

Raciocinio através de procura
Problemas de planeamento:
    Problemas cuja solução consiste numa sequência de ações a realizar e de situações
    a percorrer  para, partindo de uma situação inicial, atingir uma situação final
    (objectivo)

Sequência de ações = plano.

custo = soma dos custos das transições -> é acumulavel

procura em profundidade
decorre explorando os nós mais recentes primeiro, aumentando por isso
a profundidade do ramo corrente de procura, tal como exemplificado para
o problema do puzzle de 8 peças

-------------
propriedades em python:
anotação própria -> @property

-------------

hash -> algo que identifica
Estereótipo que indica a definição de mecanismos de identificação única

dois objetos podem ter a mesma identidade se tiverem o mesmo hash e serem da mesma classe.

fifo -> ultimos a entrar, ultimos a sair

##############################################################################################################################################################################################

aspecto chave do método procura é a fronteira

fifo -> primeiros a entrar são os primeiros a sair. Mais velhos são os primeiros a sair
lifo -> ultimo a entrar são os primeiros a sair. Mais novos saem primeiro

dimensao da solução = no inical até no final

iterables em python

def __iter__(self):
retorna o iterador

tornar classe indexavel -> getitem(self, index)

na procura em profundidade é uma usada uma fronteira fifo
a procura em largura utiliza uma fronteira lifo

memorizar grafo -> inserir na fronteira e nos explorados mas so se o nó não existir ainda

problema da contagem

dado um valor inicial, um valor final e um conjunto de 
incrementos possiveis, que incrementos realizar para atingir
ou superer ou valor final.
Para observar o efeito do custa na procura, o custo dos operadores
corresponde ao quadrado do incremento

Valor inicial = 0
Valor final = 0
Incrementos = [1,2]

na pasta mod_prob vamos incluir classes de modelo do problema


-----


VALOR_INCIAL = 0
VALOR_FINAL = 9
INCREMENTOS = [1,2]
problema = ProblemaContagem(VALOR_INCIAL, VALOR_FINAL, INCREMENTOS)

-----

Qual é a viabilidade de aplicar os métodos de raciocinio automatico com base em procura
de espaços de estados em contextos reais?

Para resolver um problema quais os recursos computacionais necessários?
    * quanto tempo necessario?
    * quanta memoria necessaria

descobrir a profundidade -> vamos fazendo procuras sucessivas aumentando a profundidade até alguma dessas
procuras encontrar solução

-----

caracterista de metodos: 
    - completo e otimo? se exitir solução, garantidamente encontrar
    - otimo? se existir solução, garantidamente a melhor
    - complexidade? no total, quantos nos vão existir na memoria?

-----
procura melhor primeira -> avalia os percursos com funçao de avalicação dos nós.
funçao f que normalmente é uma função de custo, tem um valor 0 ou >. Ao seja
quanto maior a função, pior a solução.
então tendo esta função de avaliação, preciso de ordenar os nos da fronteira
por funcao de avaliação. Os que ficam no inicio são os melhores e vao ser os primeiros
a serem explorados
----
procura de custo uniforme

caso particular de procura melhor primeiro
##############################################################################################################################################################################################

Aula 6 de Maio
Numa arquitetura reativa com memória, as reações podem manter o estado ou memória
de situações passadas desfavoráveis. Assim consegue ser mais eficiente.

Agente reativo com memória ainda não consegue planear trajetos. Vamos
integrar uma arquitetura de sistema autonomo.

Enquadramento base:
3 horizontes:
    1- Um que avança para o futuro = PASSADO - PRESENTE - FUTURO -> Agentes Deliberativos: Antecipar
    2- Um que recua no tempo = PASSADO - PRESENTE -> Agentes reativos com estado: Repetir / Evita
    3- Outro que fica no presente = Agentes reativos sem estado (ausencia de memória): Reagir

Agente não consegue simular sem a memória. Se nos introduzirmos memória, o 
horizonte alarga-se. 

Evitar o passado, repetir o passado para ser mais eficiente.

Caso geral implica 3 horizontes temporais.

Antecipar o futuro é essencial para otimizar processo.

Não há computação sem memória.

Suporte = memória

Passado = memória de recordações do passado (repetir/evitar): recordação em termos de processo cognitivo
Presente = memória de perceções e de ações atuais (reagir): 
Futuro: memória de simulação de situações e ações futuras (antecipar). Antecipar porque queremos atingir objetivos.

Processo Deliberativos -> processo em que o agente intencionalmente, simula situações
internas pelas quais pode passar.

Arquitetura de Agente Deliberativos
    Memoria -> elemento central vs agente reativo onde memória é auxiliar.
    É na memória onde será feita a simulação dos possíveis eventos
    processos cognitivos: processos de raciocínio e de decisão.
    raciocínio -> encontrar meios para realizar algo.
    decisão -> raciocínio especial do que fazer e como fazer.

    Resultado destes processos de internos -> planos de ação. 

Sistemas intencionais -> sistemas que operam por concretização de intenções.
Elemento central é o objetivo a atingir vs AR onde objetivos não eram explícitos.
Agentes deliberativos explicitam os objetivos. Se houver vários, sistema vai ter
de decidir qual é que vai realizar, pois não pode realizar 2 objetivos ao mesmo tempo.
Objetivos vão guiar todo o processamento interno do sistema.
Fins e meios: Fins -> aquilo que se pretendo atingir
              Meios -> recursos que usamos para atingir os fins.

raciocínio sobre os meios -> planeamento que vai dar origem sobre os meios.
raciocínio sobre os fins -> 

Qualquer sistema tem de ter conhecimento para conseguir antecipar de tudo.
conhecimento ou vem da experiência do agente (agente que tenha memória)
ou vem de algo que já tem esse conhecimento e o transmite (programador que informa).

Modelo do mundo vai ser a base para dar essa informação. Qualquer agente Deliberativo
precisa desse modelo interno para ser fazer simulações.

Planos de ações: sequencias de ações pela quais o agente tem de passar para
atingir certo objetivo. Podem ser só ações, mas neste caso agente não consegues
saber se são os mais adequados. 

Raciocínio Automático:
O processo de raciocínio automático envolve dois tipos de atividades
principais, a exploração de opções possíveis e a avaliação de opções para
decisão acerca das melhores opções. Até agora, a avaliação das opções tem sido
por custo, o que é que o agente tem a perder. Mas há outra forma -> Maximizar o ganho.

Há várias áreas do raciocínio automático:
raciocínio teórico -> resolver equação, tenho conjunto de o
raciocínio prático -> raciocino orientado para a ação

raciocínio prático:
Área do raciocínio automático.
No contexto de um agente autónomo que opera num determinado ambiente, é particularmente
relevante o raciocínio orientado para a ação designado raciocínio prático.

Tem 3 raciocínios.
    1 - Objetivos a atingir.
    2 - Ações que o agente pode fazer (N, S, E, O).
    3 - Representação do mundo (ambiente, obstáculos, posições livres...).

Resultado do raciocínio = planos de ação.

Este tipo de raciocínio tem 3 vertentes:
    1 - RACIOCÍNIO SOBRE FINS (DELIBERAÇÃO) -> Pegar na representação interna e perceber quais
        é que são as o que fazer com as várias opções possíveis. E transforma em objetivos
    2 - RACIOCÍNIO SOBRE MEIOS (PLANEAMENTO) -> Pega na Representação do mundo e transforma
        em planos de ação.


Racionalidade limitada -> agente não vai procurar atingir a solução ótima mas então uma solução
suficientemente boa.

Nós vamos implementar uma racionalidade ótima, encontrar a melhor solução possível.

ARQUITECTURA DELIBERATIVA
Modelo do mundo -> memória interna

Processo de tomada de decisão:
    Suporta o processo geral de tomada de decisão que determinada o comportamento do agente,
    ou seja, quais as ações a realizar perante as perceções obtidas e o estado do modelo interno.
        1 - Observar o mundo.
        2 - Atualizar o modelo do mundo
        3 - Deliberar o que fazer
        4 - Planear gerando um plano de ação. Tendo sido produzido um plano, já não preciso
        deliberar o que fazer nem planear outra vez. A não ser que aconteça que o ambiente
        mude dinamicamente.
        5 - Executar o plano de ação
    
    Quando os ambientes são muitos dinâmicos, o processamento interno pode não conseguir
    acompanhar e os planos depois já não são bons. 
    Temos que garantir se o resultado do sistema é permanentemente bom 

Reconsideração:
Se o mundo se alterou ou se não houver planos, fazemos reconsideração.
Revalidação de opções com eventual mudança de planos. Função interna do sistema
que perante as situações atuais decide de é necessário reconsiderar. Se não, o agente pode continuar
com os planos originais

Adicionamos o passo:
    3. Se reconsiderar.
        4. Deliberar
        5- Planear

Controlo -> aquele que coordena as atividades internas do sistema. Onde vai estar o processo
de tomada de decisão.

Estado do agente tem associado uma posição para efeitos de simulação e processo interno do agente.

##############################################################################################################################################################################################
Aula 13 de Maio

Procura em espaço de estados -> proporciona um dominio da representação. Sistema vai observar o espaço 
de estados e vai escolher um percurso e depois vai dar origem ao plano.

Modelo do problema:
    Estado -> posição do agente
    Operador -> Define as transformaç~pes de estado deste problema
    Problema -> Indica o estado inicial, o critierio para o estado ser objetivo...
    Solução -> percurso
    
Planeamento automático -> processo deliberativo que tem por objetivo gerar sequências de ação = planos
para atingir objetivos pré definidos.

Planamento -> feito com base em métodos de raciocionio automatico (ex: pee).

Processo de planeamento precisa de um modelo de planeamento e os objetivos a atingir

Há no entanto problemas de planeamento
O racíocinio auto, através da procura, opera na resolução de problemas de pplaneamento tendo por base
uma abstração do domínio do problema -> ESPAÇO DE ESTADOS.
Espaço de estados: cada configuração possivel na resolução do problema = ESTADO onde as 
várias ações que produzem as transformações de uma configuração para outra -> OPERADORES
Operadores -> quando aplicados, originam transições de estado gerando novos estados.

##############################################################################################################################################################################################
Aula 20 de Maio
Processos de decisão sequencial

No problema geral de tomada de decisão por um agente que opera num determinado mundo,
os estados e açoes do agente vão-se alterando ao longo do tempo, em função das
decisões do agente, das ações selecionadas, e dos resultados dessas ações

Num processo de decisão geral, para cada estado sn, cada decisão

A inceerteza resulta da impossibilidade de se obter info completa relativa ao dominio
do problema. Exemplo: navegação em veiculos autonomos.

Não determinista: com determinada probabilidade faz esta coisa

Sistema vai estar sempre a vir para o estado atual. Sistema consegue antecipar
futuros possiveis -> é isso que os diferente ramos mostram.

agente evolui fazendo ações. 
Precisamos de incomrpar a incerteza. Quando ocorre uma ação, não produz
uma unica ação determinista para um estado mas várias ações com uma probabilidade

propriedade de markov -> evolução de cada dos estados só pode depender do estado atual.
Não pode depender de estados passados. Se nos tivermos essa propriedade passamos a 
ter processo de decisão de markov que é processo de decisão sequencial que satisfaz 
a propriedade de markov

modelo de transição -> representado pela função t
da nos a info das probabilidades das transições de estado por efeito de ação A
função de recompensa -> representado pela função r qual a recompensa numa transição

utilidade -> valor de longo prazo de historia de evolução, de estar num 
estado para efietos de concretização dos objetivos do sistama

recompensa -> ganhos e perdas locais

S = {s0, s1, s2}
pol : S -> A(s) formato geral de função
pol(s: S): A
'''
# Executar simulador da SAE
#from agente.agente_delib_pee import AgenteDelibPEE
from agente.controlo_delib.agente_delib_pdm import AgenteDelibPDM
from sae import Simulador
from agente.agente_reactivo import AgenteReactivo as Agente


Simulador(1, AgenteDelibPDM()).executar()