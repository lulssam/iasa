from deposito.deposito_agua import DepositoAgua
from pee.mec_proc.solucao import Solucao
from pee.melhor_primeiro.procura_custo_unif import ProcuraCustounif

# instanciar problema
problema = DepositoAgua(0,9)
# instanciar mecanismo de procura custo uniforme
mec_proc = ProcuraCustounif()
# produzir solução com esse mecanismo de procura
solucao = mec_proc.solucao()
print(solucao)

