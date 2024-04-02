
Hashtable = {}

MAX_HASHTABLE = 10

#Funcao que adiciona os arquivos ao cache
def addCache(arquivo,cachehit,cachemiss):
  #Se o arquivo ja estiver no cache, adicionará + 1 a sua frequência
  InCache = checkCache(arquivo)
  if InCache:
    return cachehit + 1, cachemiss

  else:
    #Caso a HashTable esteja cheia
    if len(Hashtable) >= MAX_HASHTABLE:
      KeysPresent = checkHash()
      print(KeysPresent)

      #Numero escolhido apenas para garantir que terá uma frequência menor que ele
      menorFrequencia = 10000
      menorFrequenciaKey = KeysPresent[0]
      for i in KeysPresent:

        if Hashtable[i] < menorFrequencia:
          menorFrequencia = Hashtable[i]
          menorFrequenciaKey = i

      #Retira o arquivo com a menor frequência
      Hashtable.pop(menorFrequenciaKey)
      Hashtable[f'textos/{arquivo}.txt'] = 1

    #Caso ainda possua espaço na HashTable
    else:
      Hashtable[f'textos/{arquivo}.txt'] = 1
    return cachehit, cachemiss + 1


#Checa se o arquivo já está no HashTable
def checkCache(arquivo):
  if f'textos/{arquivo}.txt' in Hashtable:
    Hashtable[f'textos/{arquivo}.txt'] += 1
    return True

#Checa todas as chaves que estão dentro do Hashtable
def checkHash():
  KeysPresent = []
  for i in range(1, 100):
    if f'textos/{i}.txt' in Hashtable:
      KeysPresent.append(f'textos/{i}.txt')
  return KeysPresent