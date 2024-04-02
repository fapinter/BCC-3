from collections import deque

queue = deque()
#implementacao de LRU com queues

MAX_QUEUE = 10

def addCache(x, cachehit, cachemiss):
    InQueue = checkCache(x)
    if InQueue:
        queue.remove(f'textos/{x}.txt')
        queue.append(f'textos/{x}.txt')
        return cachehit + 1, cachemiss
    
    else:
        if len(queue) >= MAX_QUEUE:
            queue.popleft()
            queue.append(f'textos/{x}.txt')
        else:
            queue.append(f'textos/{x}.txt')

        return cachehit, cachemiss + 1

def checkCache(x):
    if f'textos/{x}.txt' in queue:
        return True