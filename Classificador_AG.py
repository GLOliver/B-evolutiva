#Individuo
#Vetor de regras quaternario de 7 algarismos (Tamanho do vetor = 4^7= 16.384‬);

import random
import math

tam = 16384
numConfig = 100 #(GLOBAL) Número de configurações
tamConfig = 35 #(GLOBAL) Tamanho da configuração

class AG:
    def __init__(self, tamPopulacao, numGeracao):
        self.tamPopulacao = int(tamPopulacao)
        self.numGeracao = int(numGeracao)
        self.populacaoInicial = []
        self.populacao = []
        self.configuracoes = []
        
        self._encodeBaseFour([0,0,0,0,0,1,1])

        #self._initPopulacao()
        #self._initConfigs()

    def _initPopulacao(self):
        for i in range(0,self.tamPopulacao):
            inidividuo = [] #regra quaternaria;
            inidividuo.append(0) #Fitness inicial(zero) adicionado na primeira posição do array;
            for j in range(0, tam):
                rdm = random.randint(0, 3)
                inidividuo.append(rdm)
            
            self.populacaoInicial.append(inidividuo)
        print("(RETIRAR) Tamanho da população inicial: ", len(self.populacaoInicial))

    def _initConfigs(self):
        for i in range(0, numConfig):
            config = []
            for j in range(0, tamConfig):
                rdm = random.randint(0, 1)
                config.append(rdm)
            
            self.configuracoes.append(config)
        print("(RETIRAR) Tamanho da coleção de configurações: ", len(self.configuracoes))

    def _encodeBaseFour(self, listBase):
        baseFour = [0,1,2,3,4,5,7,8]
        res = 0
        numEncode = list(listBase)
        numEncode.reverse()
        for i,j in enumerate(numEncode):
            res += baseFour.index(i) * 4**(j)
        
        print("A resposta é: ", res)
        #return res

    def _decodeBaseFour(self, decimal):
        decimal = 1


#--------------------- Main ----------------
if __name__ == '__main__':
    print("Input de dados...")
    tamP = input("Tamanho da Populacao: ")
    numG = input("Número de gerações: ")
    ag = AG(tamP, numG)