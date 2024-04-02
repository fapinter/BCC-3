from collections import deque

#TAMANHO DO CACHE
MAX_QUEUE = 10
queue = deque()


#FUNCAO PARA CHECAR SE X elemento esta na queue
def checkCache(x):
  if f'{x}.txt' in queue:
    
    return True
    

#FUNCAO PARA ADICIONAR NA QUEUE
def addCache(x, cachehit, cachemiss):
  InQueue = checkCache(x)
  if InQueue:
    return cachehit + 1, cachemiss
  else:
    if len(queue) >= MAX_QUEUE:
      queue.popleft()
      queue.append(f'{x}.txt')
    else:
      queue.append(f'{x}.txt')
    return cachehit, cachemiss + 1