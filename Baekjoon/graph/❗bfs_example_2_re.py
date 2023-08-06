'''
1, 1 : 현재 위치
N, M : 탈출 좌표
1 : 이동 가능
0 : 이동 불가
task : 최소 이동 수
=> 간선의 비용이 모두 같을 때 최소경로 : 'BFS'
'''
from collections import deque

def bfs_legacy(matrix, node, visited):
    queue = deque([node])
    visited[node] = True
    print(node, end = ' ')
    
    while queue :
        node = queue.popleft()
        for adj_node in matrix[node] :
            if adj_node not in visited :
                queue.append(adj_node)
                visited[adj_node] = True
                print(adj_node, end = ' ')

# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
                
def bfs(matrix, x, y):
    queue = deque()
    queue.append((x,y)) # 튜플일경우 이렇게 해야함. 처음부터 선언은 불가
    matrix[x-1][y-1] = 1
    
    while queue :
        x, y = queue.popleft()
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            # 공간제한
            if nx < 0 or ny < 0 or nx >= n or ny >= m :
                continue
            # 문제제한
            if matrix[nx][ny] == 0:
                continue
            # 이웃이 방문처리가 안된 경우 (즉 아직 미방문. 지금이 첫 방문 경우)
            if matrix[nx][ny] == 1 :
                queue.append((nx, ny))
                matrix[nx][ny] = matrix[x][y] + 1
    return matrix[n-1][m-1]


if __name__ == '__main__' :
    n,m = map(int, input().split())
    graph = []
    for i in range(n):
        graph.append(list(map(int, input())))
    result = bfs(graph, 0, 0)
    print(result)
    
'''
5 6
101010
111111
000001
111111
111111
'''