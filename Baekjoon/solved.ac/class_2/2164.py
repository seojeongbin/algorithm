'''
큐
1234
234 -> 342
42 -> 24
4
문제설명에서 선입선출, 후입선출 이런걸 설명하는 듯한 뉘앙스면 가장 우선시하게 떠올리기
큐는 양쪽다 된단걸 생각
'''

from collections import deque 

N = int(input())
array = [i+1 for i in range(N)]
queue = deque(array) # 리스트를 통한 초기화

cnt = 0
while len(queue)>1 :    
    # 버리고
    queue.popleft()
    # 옮기고
    var = queue.popleft()
    queue.append(var)
    
print(queue[0])