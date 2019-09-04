#Individuo
#Vetor de regras quaternario de 7 algarismos (Tamanho do vetor = 4^7= 16.384‬);

import random
import math

tam = 16384
numConfig = 100 #(GLOBAL) Número de configurações
tamConfig = 35 #(GLOBAL) Tamanho da configuração

#Configuração = Objeto que contem a configuração em sí e o estado que ela deve ter no final

class AG:
    def __init__(self, tamPopulacao, numGeracao):
        self.tamPopulacao = int(tamPopulacao)
        self.numGeracao = int(numGeracao)
        self.populacaoInicial = []
        self.populacao = []
        self.configuracoes = []
        
        #print(self._encodeBaseFour([3,3,3,3,3,3,3]))

        print("Iniciando população de regras ...")
        self._initPopulacao()
        print("População de regras iniciada ...")
        self._initConfigs()

        testeConfig = self.configuracoes[0]
        testePopulacao = self.populacaoInicial[0]

        self._runAutomato(testePopulacao,testeConfig,5)


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
        baseFour = [0,1,2,3,4,5,6,7,8]
        res = 0
        numEncode = list(listBase)
        numEncode.reverse()
        for i in range(0 , len(numEncode)):
            res += int(numEncode[i]) * 4**int(baseFour[i])
        
        #print("(RETIRAR)A resposta é: ", res)
        return res

    #def _decodeBaseFour(self, decimal): (IMPLEMENTAR SE FOR PRECISO)

    def _runAutomato(self, regra, config, numTimeStap):
        for i in range(0,numTimeStap):
            newConfig = config.copy()
            print("Configuração original: ", config)
            #Inserindo os três ultimos nos três primeiros
            newConfig.insert(0,config[len(config)-1])
            newConfig.insert(0,config[len(config)-2])
            newConfig.insert(0,config[len(config)-3])
            #Adicionando os três primeiros nos três ultimos
            newConfig.append(config[0])
            newConfig.append(config[1])
            newConfig.append(config[2])
            print("Configuração original(com os 6 valores a mais): ", newConfig)
            
            posicao = 0
            for j in range(3, len(config)+3):
                newRegra = [newConfig[j-3],newConfig[j-2],newConfig[j-1],newConfig[j],newConfig[j+1],newConfig[j+2],newConfig[j+3]]
                codeDecimal = self._encodeBaseFour(newRegra) + 1
                config[posicao] = regra[codeDecimal+1]
                posicao += 1
            print(config)





#--------------------- Main ----------------
if __name__ == '__main__':
    print("Input de dados...")
    tamP = input("Tamanho da Populacao: ")
    numG = input("Número de gerações: ")
    ag = AG(tamP, numG)