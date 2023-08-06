# 그림과 같은 경우에서 방문순서 출력하기
'''
- while queue 쓴다는거 밖에 차이가 없다!
- queue를 정의(혹은 append) 하는 구간에서 방문처리 및 프린트 한다
- 코테에 대비해서는 이해하려고 하지말고 dfs, bfs는 무지성 암기가 좋을듯
'''

def dfs(matrix, start_node, visited):
    visited[start_node] = True
    print(start_node, end = ' ')
    for i in matrix[start_node]:
        if visited[i] == False :
            dfs(matrix, i, visited)

from collections import deque

def bfs(matrix, node, visited) : 
    queue = deque([node])
    visited[node] = True
    print(node, end = ' ')
    while queue :
        node = queue.popleft()
        for i in matrix[node] :
            if visited[i] == False :
                queue.append(i)
                visited[i] = True
                print(i, end = ' ')
    
    
    
if __name__ == '__main__' :
    
    matrix = [
        [], 
        [2,3,8],
        [1,7],
        [1,4,5],
        [3,5],
        [3,4],
        [7],
        [2,6,8],
        [1,7]    
    ]

    visited = [False]*len(matrix)
    
    # dfs(matrix, 1, visited)
    bfs(matrix, 1, visited)