# 그림과 같은 경우에서 방문순서 출력하기
'''
1. 인접행렬
2. 노드별 방문여부 리스트
3. 이웃별로 for문으로 순차적 돌리는게 곧 dfs(stack)의 원리
'''
matrix = [
    [], # 0번 노드란 없으니. 이게 더 편하게 표현가능이란다
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]    
]

visited = [False] * len(matrix)

def dfs(matrix, node, visited):
    # 1. 일단 현재 노드를 방문 처리한다
    visited[node] = True
    print(node, end = ' ')
    # 2. 그 노드의 이웃에 대해 재귀적 방문 => for 걸린 하나에 대해 재귀쓴다는게 곧 dfs
    for i in matrix[node]:
        if visited[i] == False :
            dfs(matrix, i, visited)
            
if __name__ == "__main__" :
    dfs(matrix, 1, visited)
