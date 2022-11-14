'''
level : silver 3
type : dfs
<문제 설명>
- 입력) 노드 수, 링크 수
- 다음줄부터는 연결 된 노드
- 출력) 1번 컴퓨터를 통해 바이러스에 걸리게 되는 컴퓨터 수
'''
import sys

num_node = int(input())
num_link = int(input())

graph = [[] for _ in range(num_node+1)]
visited = [0]*(num_node+1)

for _ in range(num_link):
    tmpL=list(map(int,sys.stdin.readline().split()))
    graph[tmpL[0]].append(tmpL[1])
    graph[tmpL[1]].append(tmpL[0])
    
# print(graph)

def dfs(graph, node, visited):
    visited[node]=1
    for nei_node in graph[node]:
        if visited[nei_node] == 0 :
            dfs(graph, nei_node, visited)
            
if __name__ == "__main__" :
    dfs(graph, 1, visited)
    # print(f'visited : {visited}')
    result = sum(visited) - 1
    # print(f'result : {result}')
    print(result)