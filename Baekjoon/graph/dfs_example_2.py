import sys
sys.setrecursionlimit(10**7)

# 문제 공간이 인접행렬로 표현못하고 좌표행렬인 경우 => matrix가 인접행렬이 아닌 지형정보
'''
1. 인접행렬 => 지형정보 matrix
2. 노드별 방문여부 리스트 => X. 이 경우 matrix가 곧 방문여부 포함함
3. 이웃별로 for문으로 순차적 돌리는게 곧 dfs(stack)의 원리
- 현재위치에서 dfs로 처음 방문하게 되는 경우 & 역시나 방문하면 0 => 1
** matrix 공간 문제는 세로방향이 x인게 좋다 => graph[x][y] 인덱싱 때문에 그렇다!!
=> dfs 사용 판단이 서면, 뭘하든 1) 현재 방문처리 2) 이웃한 것들을 재귀적으로 방문처리 
'''

# visited = [False] * len(matrix)

def dfs_prior(matrix, node, visited):
    # 1. 일단 현재 노드를 방문 처리한다
    visited[node] = True
    print(node, end = ' ')
    # 2. 그 노드의 이웃에 대해 재귀적 방문 => for 걸린 하나에 대해 재귀쓴다는게 곧 dfs
    for i in matrix[node]:
        if visited[i] == False :
            dfs_prior(matrix, i, visited)

def dfs(x, y, graph):
    # 문제가 공간정보를 담은 틀이라면 틀 범위 벗어나는 경우 처리 필요
    if x<0 or x>=n or y<0 or y>=m:
        return False
    if graph[x][y] == 0 :
        # 1. 방문처리
        graph[x][y] = 1
        # 2. 이웃한거에 대해 재귀적 방문
        dfs(x-1, y, graph)
        dfs(x+1, y, graph)
        dfs(x, y-1, graph)
        dfs(x, y+1, graph)
        return True 
    return False

if __name__ == "__main__" :
    n, m = 4, 5
    matrix = [[0, 0, 1, 1, 0], [0, 0, 0, 1, 1], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0]]
    
    cnt = 0
    for i in range(n):
        for j in range(m):
            # 각 위치에서 dfs 수행 => 처음 수행된거라면 += 1
            if dfs(i,j, matrix) == True :
                cnt += 1
    
    print(cnt)

