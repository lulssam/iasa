from lib.mod.estado import Estado

'''Classe que '''
class EstadoPuzzle(Estado):
    def _init_(self,configuraccao):
        self.configuraccao= configuraccao
    def id_valor(self):
        a=0
        id = 0
        for i in self.configuraccao:
           id +=  10*a*i
           a+=1
        return id

puzzle = EstadoPuzzle([4,2,6,2,5,7,1,8,0])
print(puzzle.id_valor())