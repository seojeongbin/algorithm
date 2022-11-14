'''
level : silver 2
type : bfs
<문제 설명>
- 입력) 노드 수, 링크 수, 시작 노드 번호
- 다음줄부터는 연결 된 노드
- 출력) 노드별 방문순서
'''

from collections import deque
import sys
sys.setrecursionlimit(10**9)  


num_node, num_link, root_node = map(int, input().split())
graph = [[] for _ in range(num_node+1)]
visited = [0] * (num_node + 1)


# for _ in range(num_link):
#     node_1, node_2 = map(int, input().split())
#     graph[node_1].append(node_2)
#     graph[node_2].append(node_1)

# 입출력 이거로 바꾸니까 시간문제 잘 되네 ㅇㅇ    
for _ in range(num_link):
    tmpL=list(map(int,sys.stdin.readline().split()))
    graph[tmpL[0]].append(tmpL[1])
    graph[tmpL[1]].append(tmpL[0])
    
for i in range(num_node+1):
    graph[i].sort() 

# print(graph)

cnt = 1
def bfs(graph, node, visited) :
    global cnt 
    queue = deque([node])
    visited[node] = cnt
    
    while queue:
        v = queue.popleft()
        for neighbor_node in graph[v]:
            if visited[neighbor_node] == 0 :
                cnt += 1
                queue.append(neighbor_node)
                visited[neighbor_node] = cnt

if __name__ == "__main__" :
    
    bfs(graph, root_node, visited)
    for i in range(1, num_node+1):
        print(visited[i])