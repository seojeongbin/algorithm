import sys
from collections import deque

queue = deque()

def push(num):
    queue.append(num)

def task(kind):
    if kind == 'pop':
        if len(queue) > 0 :
            return queue.popleft()
        else :
            return -1
    elif kind == 'size':
        return len(queue)
    elif kind == 'empty':
        if len(queue) == 0:
            return 1
        else :
            return 0
    elif kind == 'front':
        if queue :
            return queue[0]
        else :
            return -1
    elif kind == 'back':
        if queue :
            return queue[-1]
        else :
            return -1    

if __name__ == "__main__" :
    
    N = int(input())
    for _ in range(N):
        command = sys.stdin.readline().split()
        if command[0] == 'push':
            push(command[1])
        else :
            result = task(command[0])
            print(result)