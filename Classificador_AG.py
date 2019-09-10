#Individuo
#Vetor de regras quaternario de 7 algarismos (Tamanho do vetor = 4^7= 16.384‬);

import random
import math

tam = 16384 #(GLOBAL) Número de elementos no vetor de regras
numConfig = 100 #(GLOBAL) Número de configurações
tamConfig = 35 #(GLOBAL) Tamanho da configuração
timeStamp = 100 #(GLOBAL) Numero de vezes que a configuração será submetido a regra (Time Stamp)

#Configuração = Objeto que contem a configuração em sí e o estado que ela deve ter no final
class Individuo:
    pass

class Configuracao:
    pass

class AG:
    def __init__(self, tamPopulacao, numGeracao):
        self.tamPopulacao = int(tamPopulacao)
        self.numGeracao = int(numGeracao)
        self.populacaoInicial = []
        self.populacao = []
        self.configuracoesInicial = []
        self.configuracoes = []
        
        #print(self._encodeBaseFour([3,3,3,3,3,3,3]))

        print("Iniciando população de regras ...")
        self._initPopulacao()
        print("População de regras iniciada ...")
        self._initConfigs()

        self.configuracoes = self.configuracoesInicial.copy()
        self.populacao = self.populacaoInicial.copy()

        testeConfig = self.configuracoes[0]
        testePopulacao = self.populacaoInicial[0]

        print(" ")
        print("Config: ",self.configuracoes[0].config)
        print("EstadoFinal: ",self.configuracoes[0].estadoFinal)
        print("Qtd de numeros certos: ",self.configuracoes[0].nota)
        print("Qtd de Numeros originais: ",self.configuracoes[0].qtd)
        self._runAutomato(0,0,timeStamp)
        print("Config: ",self.configuracoes[0].config)
        print("EstadoFinal: ",self.configuracoes[0].estadoFinal)
        print("Qtd de numeros certos: ",self.configuracoes[0].nota)
        print("Qtd de Numeros originais: ",self.configuracoes[0].qtd)
        
        print(" ")
        print("Fitness: ",self.populacao[0].fitness)
        self._calcFitness()
        print("Fitness: ",self.populacao[0].fitness)


    def _initPopulacao(self):
        for _ in range(0,self.tamPopulacao):
            regra = [] #regra quaternaria;
            fitness = 0 #inidividuo.append(0) #Fitness inicial(zero) adicionado na primeira posição do array;
            for _ in range(0, tam):
                rdm = random.randint(0, 3)
                regra.append(rdm)
            regra.append(0)
            individuo = Individuo()
            individuo.regra = regra
            individuo.fitness = fitness
            self.populacaoInicial.append(individuo)
        print("(RETIRAR) Tamanho da população inicial: ", len(self.populacaoInicial))

    def _initConfigs(self):
        for _ in range(0, numConfig):
            config = []
            for _ in range(0, tamConfig):
                rdm = random.randint(0, 1)
                config.append(rdm)
            
            configuracao = Configuracao()
            configuracao.config = config
            cont1 = 0
            cont0 = 0
            for i in range(0,len(config)):
                if (config[i] == 1):
                    cont1 = cont1 + 1
                elif (config[i] == 0):
                    cont0 = cont0 + 1
            
            if (cont0 > cont1):
                configuracao.estadoFinal = 0
                configuracao.qtd = cont0
            else:
                configuracao.estadoFinal = 1
                configuracao.qtd = cont1                

            configuracao.nota = 0
            self.configuracoesInicial.append(configuracao)
        print("(RETIRAR) Tamanho da coleção de configurações: ", len(self.configuracoesInicial))

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

    def _avaliacao(self, individuo, numIndividuo):
        const = 0


    def _runAutomato(self, numRegra, numConfig, numTimeStap):
        """ print(config)
        print(self.configuracoes[numConfig].config)
        print(self.configuracoes[numConfig].estadoFinal)
        print(self.configuracoes[numConfig].nota)
        print(self.configuracoes[numConfig].qtd) """
        regra = self.populacao[numRegra].regra
        regra.reverse() #Colocando o vetor em ordem lexicográfica
        config = self.configuracoes[numConfig].config
        for _ in range(0,numTimeStap):
            #print(i)
            newConfig = config.copy()
            #print("Configuração original: ", config)
            #Inserindo os três ultimos nos três primeiros
            newConfig.insert(0,config[len(config)-1])
            newConfig.insert(0,config[len(config)-2])
            newConfig.insert(0,config[len(config)-3])
            #Adicionando os três primeiros nos três ultimos
            newConfig.append(config[0])
            newConfig.append(config[1])
            newConfig.append(config[2])
            #print("Configuração original(com os 6 valores a mais): ", newConfig)
            
            posicao = 0
            for j in range(3, len(config)+3):
                newSeguimento = [newConfig[j-3],newConfig[j-2],newConfig[j-1],newConfig[j],newConfig[j+1],newConfig[j+2],newConfig[j+3]]

                codeDecimal = self._encodeBaseFour(newSeguimento) + 1
                config[posicao] = regra[codeDecimal]
                posicao += 1
            #print(config)
        self.configuracoes[numConfig].config = config
        if(self.configuracoes[numConfig].estadoFinal == 0):
            cont0 = 0
            for i in range(0,len(config)):
                if(config[i] == 0):
                    cont0 = cont0 + 1
            self.configuracoes[numConfig].nota = cont0
        else:
            cont1 = 0
            for i in range(0,len(config)):
                if(config[i] == 1):
                    cont1 = cont1 + 1
            self.configuracoes[numConfig].nota = cont1
        
        """ print(self.configuracoes[numConfig].config)
        print(self.configuracoes[numConfig].estadoFinal)
        print(self.configuracoes[numConfig].nota)
        print(self.configuracoes[numConfig].qtd) """

    def _calcFitness(self):
        for i in range(0, len(self.populacao)):
            fitness = 0
            for j in range(0, len(self.configuracoes)):
                self._runAutomato(i,j,timeStamp)
                fitness = fitness + self.configuracoes[j].nota
            self.populacao[i].fitness = fitness

    #def _selecao(self):

#--------------------- Main ----------------
if __name__ == '__main__':
    print("Input de dados...")
    tamP = input("Tamanho da Populacao: ")
    numG = input("Número de gerações: ")
    ag = AG(tamP, numG)