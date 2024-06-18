from pee.melhor_primeiro.procura_melhor_prim import ProcuraMelhorPrim


class ProcuraInformada(ProcuraMelhorPrim):
    # Vai retornar um objeto tipo Solução
    def procurar(self, problema ,heuristica):
        self._avaliador.definir_heuristica(heuristica)
        print(self._avaliador)
        return super().procurar(problema)