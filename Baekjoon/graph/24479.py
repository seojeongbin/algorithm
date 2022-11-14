'''
level : silver 2
type : dfs
<문제 설명>
- 입력) 노드 수, 링크 수, 시작 노드 번호
- 다음줄부터는 연결 된 노드
- 출력) 노드별 방문순서
<about dfs>
- 인접행렬로 표현하든지, (문제가 틀이 있는 형태경우) 리스트로 정보를 받든.. graph 위치 정보 정의가 먼저임
- 방문여부를 체크할 것도 필요. 노드번호별로 뭔가를 만들거나, 틀에 방문한여부(= 이동불가 체크)를 하거나
'''

'''
<입력>
5 5 1
1 4
1 2
2 3
2 4
3 4
'''

## 1. 값 입력 받아서 graph 구조, visited 여부 생성

num_node, num_link, root_node = map(int, input().split())
# num_node, num_link, root_node = 5, 5, 1
graph = [[] for _ in range(num_node+1)] # ★2d list 생성 시 주의 ! graph = [[]]*(num_node+1) => 이렇게하면 append썼을때 전부 다 적용되게 됨!!
visited = [0] * (num_node + 1)

for _ in range(num_link):
    node_1, node_2 = map(int, input().split())
    graph[node_1].append(node_2)
    graph[node_2].append(node_1)

for i in range(num_node+1):
    graph[i].sort() # ★ 이거 안하면 틀림 (동일할 경우 오름차순으로.. 값 작은거부터 방문하니까!!)

## 2. DFS 메서드 정의

cnt = 1
def dfs(graph, node, visited) :
    global cnt # ★ 개중요
    
    visited[node] = cnt

    for neighbor_node in graph[node]:
        if visited[neighbor_node] == 0:
            cnt += 1
            dfs(graph, neighbor_node, visited)

## 3. 출력
if __name__ == "__main__" :
    
    import sys
    sys.setrecursionlimit(10**9)  # 재귀 허용 깊이를 수동으로 늘려주는 코드 (백준 제출 용)
    
    dfs(graph, root_node, visited)
    for i in range(1, num_node+1):
        print(visited[i])
        
'''
계속 '시간 초과' 이슈가 있었음
결국 시간초과는 해결못하고 구글링 정답으로 걍 냈음..
지금이야 공부용으로 하더라도 나중에는 시간관련해서도 생각해봐야함!
'''
# 입출력 이렇게 하면 해결됨.
for _ in range(num_link):
    tmpL=list(map(int,sys.stdin.readline().split()))
    graph[tmpL[0]].append(tmpL[1])
    graph[tmpL[1]].append(tmpL[0])