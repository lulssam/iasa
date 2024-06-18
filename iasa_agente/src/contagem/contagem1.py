from mod_prob.problema_contagem import ProblemaContagem
from pee.prof.fronteira_lifo import FronteiraLIFO
from pee.prof.procura_profundidade import ProcuraProfundidade

'''
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

'''

VALOR_INCIAL = 0
VALOR_FINAL = 9
INCREMENTOS = [1,2]
problema = ProblemaContagem(VALOR_INCIAL, VALOR_FINAL, INCREMENTOS)

# fronteira_lifo = FronteiraLIFO()

mec_proc = ProcuraProfundidade()

solucao = mec_proc.procurar(problema)

# Mostrar solução
if solucao:
    print("Tem solução")
    for passo in solucao:
        print(passo.estado.id_valor(), passo.operador._incremento)