
from pdm.pdm import PDM
from modelo_pdm_teste import ModeloPDMTeste

'''
Classe de teste
'''
gama = 0.5
delta_max = 0.0
modelo_pdm = ModeloPDMTeste()
pdm = PDM(modelo_pdm, gama, delta_max)
utilidade, politica = pdm.resolver()

print(utilidade)
print(politica)
    