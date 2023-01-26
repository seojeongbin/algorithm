'''
리스트로 어떻게든 해보려다가 실패..
❗자료구조로 풀릴 것 같은건 무조건 자료구조로 풀려고하는게 훨낫다
이 문제는 circularly queue 향기가 잔뜩났다 => <queue> 써주기
'''

N, K = map(int, input().split())

from collections import deque 
queue = deque()

# [1,2,3,4,5,6,7] 이 queue 형태로 있는 상태
for i in range(1, N+1):
    queue.append(i)
    
result = []
while queue :
    # k-1(1,2번째) 까지는 살리고 (이후에도 활용하게 되니까) 뒤로 붙인다
    # 이게 circularly할때 queue 활용법!
    for _ in range(K-1): 
        queue.append(queue.popleft())
    result.append(queue.popleft())
    
# 출력 포맷팅
print('<',end='')
for elem in result[:-1] :
    print(elem, end=', ')
print(f'{result[-1]}>')


