import LFU
import LRU
import FIFO
import random
import time
import numpy as np


#O arquivo modo simulação simula todos os 3 algoritmos de cache para verificar qual o melhor
#para o aplicativo, ele pode demorar entre 5 a 7 minutos para rodar por completo devido aos
#prints dos textos que colocamos para dar mais veracidade à simulação do usuário pedindo o texto
#e sendo gerado na tela
def modoSimulacao():
  vetorAlgoritmos = [FIFO, LFU, LRU]
  vetorNomeAlgoritmos = ["FIFO", "LFU", "LRU"]
  relatorio = open('relatorio.txt', 'w', encoding='utf-8-sig')
  relatorio.write("RELATORIO DO MODO SIMULACAO\n")
  vetorTempoAlgoritmos = list()
  vetorCacheHitAlgoritmos = list()

  #Loop dos 3 algoritmos
  for i in range(0, 3):
    algoritmo = vetorAlgoritmos[i]
    CacheHitAlgoritmo = 0
    CacheMissAlgoritmo = 0

    VetorHitUsuarios = list()
    VetorMissUsuarios = list()
    VetorTempoUsuarios = list()

    VetorHitSorteio = list()
    VetorMissSorteio = list()
    VetorTempoSorteio = list()
    #Loop dos 3 usuários
    for j in range(0, 3):

      CacheHitUsuario = 0
      CacheMissUsuario = 0
      #Loop para os 3 sorteios
      for k in range(0, 3):
        match k:
          case 0:
            inicioTempPuro = time.time()
            CacheHitPuro = 0
            CacheMissPuro = 0
            for _ in range(200):
              numero = random.randint(1, 100)
              CacheHitPuro, CacheMissPuro = algoritmo.addCache(
                  numero, CacheHitPuro, CacheMissPuro)
              with open(f"textos/{numero}.txt", 'r') as arquivo:
                print(arquivo.readlines())

            VetorHitSorteio.append(CacheHitPuro)
            VetorMissSorteio.append(CacheMissPuro)
            fimTempPuro = time.time()
            TempoPuro = fimTempPuro - inicioTempPuro
            VetorTempoSorteio.append(TempoPuro)

          case 1:
            inicioTempPoison = time.time()
            CacheHitPoison = 0
            CacheMissPoison = 0
            for _ in range(200):
              numero = np.random.poisson(50)
              while numero < 1 or numero > 100:
                numero = np.random.poisson(50)
              CacheHitPoison, CacheMissPoison = algoritmo.addCache(
                  numero, CacheHitPoison, CacheMissPoison)
              with open(f"textos/{numero}.txt", 'r') as arquivo:
                print(arquivo.readlines())

            VetorHitSorteio.append(CacheHitPoison)
            VetorMissSorteio.append(CacheMissPoison)
            fimTempPoison = time.time()
            TempoPoison = fimTempPoison - inicioTempPoison
            VetorTempoSorteio.append(TempoPoison)

          case 2:
            inicioTempProb = time.time()
            CacheHitProb = 0
            CacheMissProb = 0
            for _ in range(200):
              chance = random.random()
              if chance < 0.33:
                numero = random.randint(30, 40)
                CacheHitProb, CacheMissProb = algoritmo.addCache(
                    numero, CacheHitProb, CacheMissProb)
                with open(f"textos/{numero}.txt", 'r') as arquivo:
                  print(arquivo.readlines())
              else:
                numero = random.randint(1, 100)
                CacheHitProb, CacheMissProb = algoritmo.addCache(
                    numero, CacheHitProb, CacheMissProb)
                with open(f"textos/{numero}.txt", 'r') as arquivo:
                  print(arquivo.readlines())

            VetorHitSorteio.append(CacheHitProb)
            VetorMissSorteio.append(CacheMissProb)
            fimTempProb = time.time()
            TempoProb = fimTempProb - inicioTempProb
            VetorTempoSorteio.append(TempoProb)

      match j:
        case 0:
          CacheHitUsuario = VetorHitSorteio[0] + VetorHitSorteio[
              1] + VetorHitSorteio[2]
          CacheMissUsuario = VetorMissSorteio[0] + VetorMissSorteio[
              1] + VetorMissSorteio[2]
        case 1:
          CacheHitUsuario = VetorHitSorteio[3] + VetorHitSorteio[
              4] + VetorHitSorteio[5]
          CacheMissUsuario = VetorMissSorteio[3] + VetorMissSorteio[
              4] + VetorMissSorteio[5]
        case 2:
          CacheHitUsuario = VetorHitSorteio[6] + VetorHitSorteio[
              7] + VetorHitSorteio[8]
          CacheMissUsuario = VetorMissSorteio[6] + VetorMissSorteio[
              7] + VetorMissSorteio[8]

      VetorHitUsuarios.append(CacheHitUsuario)
      VetorMissUsuarios.append(CacheMissUsuario)

      TempoUsuario = sum(VetorTempoSorteio) / 3
      VetorTempoUsuarios.append(TempoUsuario)

    CacheHitAlgoritmo = sum(VetorHitUsuarios)
    CacheMissAlgoritmo = sum(VetorMissUsuarios)
    vetorCacheHitAlgoritmos.append(CacheHitAlgoritmo)

    TempoAlgoritmo = sum(VetorTempoUsuarios) / 3
    vetorTempoAlgoritmos.append(TempoAlgoritmo)
    #Impressão do relatório
    relatorio.write(f""""
            Algoritmo {vetorNomeAlgoritmos[i]}:

                Tempo Medio: {TempoAlgoritmo}
                Cache Hits: {CacheHitAlgoritmo}
                Cache Miss: {CacheMissAlgoritmo}
                    
                    Usuario {j-1}:
                            
                        Tempo Medio do usuário: {VetorTempoUsuarios[0]}
                        Cache Hits do usuário: {VetorHitUsuarios[0]}
                        Cache Miss do usuário: {VetorMissUsuarios[0]}

                            Modo de Sorteio puro e simples:
                                Tempo do sorteio: {VetorTempoSorteio[0]}
                                Cache Hits sorteio: {VetorHitSorteio[0]}
                                Cache Miss sorteio: {VetorMissSorteio[0]}
                        
                            Modo de Sorteio poison:
                                Tempo do sorteio: {VetorTempoSorteio[1]}
                                Cache Hits sorteio: {VetorHitSorteio[1]}
                                Cache Miss sorteio: {VetorMissSorteio[1]}

                            Modo de Sorteio com probabilidade:
                                Tempo do sorteio: {VetorTempoSorteio[2]}
                                Cache Hits sorteio: {VetorHitSorteio[2]}
                                Cache Miss sorteio: {VetorMissSorteio[2]}
                    Usuario {j}:
                            
                        Tempo Medio do usuário: {VetorTempoUsuarios[1]}
                         Cache Hits do usuário: {VetorHitUsuarios[1]}
                        Cache Miss do usuário: {VetorMissUsuarios[1]}

                            Modo de Sorteio puro e simples:
                                Tempo do sorteio: {VetorTempoSorteio[3]}
                                Cache Hits sorteio: {VetorHitSorteio[3]}
                                Cache Miss sorteio: {VetorMissSorteio[3]}
                        
                            Modo de Sorteio poison:
                                Tempo do sorteio: {VetorTempoSorteio[4]}
                                Cache Hits sorteio: {VetorHitSorteio[4]}
                                Cache Miss sorteio: {VetorMissSorteio[4]}

                            Modo de Sorteio com probabilidade:
                                Tempo do sorteio: {VetorTempoSorteio[5]}
                                Cache Hits sorteio: {VetorHitSorteio[5]}
                                Cache Miss sorteio: {VetorMissSorteio[5]}

                    Usuario {j+ 1}:
                            
                        Tempo Medio do usuário: {VetorTempoUsuarios[2]}
                        Cache Hits do usuário: {VetorHitUsuarios[2]}
                        Cache Miss do usuário: {VetorMissUsuarios[2]}

                            Modo de Sorteio puro e simples:
                                Tempo do sorteio: {VetorTempoSorteio[6]}
                                Cache Hits sorteio: {VetorHitSorteio[6]}
                                Cache Miss sorteio: {VetorMissSorteio[6]}
                        
                            Modo de Sorteio poison:
                                Tempo do sorteio: {VetorTempoSorteio[7]}
                                Cache Hits sorteio: {VetorHitSorteio[7]}
                                Cache Miss sorteio: {VetorMissSorteio[7]}

                            Modo de Sorteio com probabilidade:
                                Tempo do sorteio: {VetorTempoSorteio[8]}
                                Cache Hits sorteio: {VetorHitSorteio[8]}
                                Cache Miss sorteio: {VetorMissSorteio[8]}""")
  relatorio.close()
  if vetorTempoAlgoritmos[0] < vetorTempoAlgoritmos[
      1] and vetorTempoAlgoritmos[0] < vetorTempoAlgoritmos[2]:
    melhorTempo = vetorAlgoritmos[0]
  elif vetorTempoAlgoritmos[1] < vetorTempoAlgoritmos[
      0] and vetorTempoAlgoritmos[1] < vetorTempoAlgoritmos[2]:
    melhorTempo = vetorAlgoritmos[1]
  else:
    melhorTempo = vetorAlgoritmos[2]

  if vetorCacheHitAlgoritmos[0] > vetorCacheHitAlgoritmos[
      1] and vetorCacheHitAlgoritmos[0] > vetorCacheHitAlgoritmos[2]:
    melhorCacheHit = vetorAlgoritmos[0]
  elif vetorCacheHitAlgoritmos[1] > vetorCacheHitAlgoritmos[
      0] and vetorCacheHitAlgoritmos[1] > vetorCacheHitAlgoritmos[2]:
    melhorCacheHit = vetorAlgoritmos[1]
  else:
    melhorCacheHit = vetorAlgoritmos[2]

  if melhorTempo != melhorCacheHit:
    return melhorTempo
  else:
    return melhorCacheHit
