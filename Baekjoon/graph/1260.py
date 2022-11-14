from collections import deque
import sys
sys.setrecursionlimit(10**9)  


num_node, num_link, root_node = map(int, input().split())
graph = [[] for _ in range(num_node+1)]
visited = [0] * (num_node + 1)

for _ in range(num_link):
    tmpL=list(map(int,sys.stdin.readline().split()))
    graph[tmpL[0]].append(tmpL[1])
    graph[tmpL[1]].append(tmpL[0])
    
for i in range(num_node+1):
    graph[i].sort() 
# print(graph)

def dfs(graph, node, visited) :
    
    visited[node] = 1
    print(node, end=' ')
    
    for neighbor_node in graph[node]:
        if visited[neighbor_node]==0:
            dfs(graph, neighbor_node, visited)

def bfs(graph, node, visited) :

    queue = deque([node])
    visited[node] = 1
    
    while queue :
        v = queue.popleft()
        print(v, end=' ')
        for neighbor_node in graph[v]:
            if visited[neighbor_node]==0:
                queue.append(neighbor_node)
                visited[neighbor_node] = 1

if __name__ == "__main__" :
    
    dfs(graph, root_node, visited)
    visited = [0] * (num_node + 1) # 이거 다시 초기화 해줬음!! 다른건 아니고 이게 포인트..  
    print()
    bfs(graph, root_node, visited)
    
