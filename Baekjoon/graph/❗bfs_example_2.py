'''
1, 1 : 현재 위치
N, M : 탈출 좌표
1 : 이동 가능
0 : 이동 불가
task : 최소 이동 수
=> 간선의 비용이 모두 같을 때 최소경로 : 'BFS'
'''

# def bfs(matrix, node, visited):
#     queue = deque([node])
#     visited[node] = True
#     print(node, end = ' ')
#     while queue :
#         node = queue.popleft()
#         for adj_node in matrix[node]:
#             if adj_node not in visited :
#                 queue.append(adj_node)
#                 visited[adj_node] = True
#                 print(adj_node, end = ' ')


# 이동문제/시뮬레이션 문제는 늘 방향벡터 정의? (상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

from collections import deque

def bfs(matrix, x, y) :
    # queue = deque((x, y)) <- 이렇게는 바로 불가
    queue = deque()
    queue.append((x, y)) # 튜플로
    while queue :
        x, y = queue.popleft()
        # 이웃정보 정상 확인 (동서남북)
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            # 1. 문제조건 위배되는 경우
            if nx < 0 or ny < 0 or nx >=n or ny >= m: # 1-1. 공간을 벗어난 경우 (1-2보다 이게 먼저여야함. 여기서 먼저 컨티뉴 걸려야)
                continue
            if matrix[nx][ny] == 0 : # 1-2. 이동 못하는 경우 (0이면 문제에서 이동못한다고 함)
                continue
            # 2. 방문하지 않은 경우 (지금이 첫 방문인경우)
            if matrix[nx][ny] == 1:
                matrix[nx][ny] = matrix[x][y] + 1 # 거리값 더하는 거임 거리값. 하나씩 올라간다 했으니
                queue.append((nx, ny))
    # 목적지까지 최단 거리 반환
    return matrix[n-1][m-1]
                
if __name__ == '__main__' :
    # input
    n,m = map(int, input().split())
    graph = []
    for i in range(n):
        graph.append(list(map(int, input())))
    result = bfs(graph, 0, 0)
    print(result)
    