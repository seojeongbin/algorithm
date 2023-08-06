'''
유형 : BFS => 역시나 떠올리는게 가장 중요 ❗
레벨 : 실버1
- 걷기 : +, - 1
- 이동 : 현위치 2배
=> 수빈이와 동생의 위치가 주어졌을때 찾는 가장 빠른 시간 몇초?
'''

'''
아마 흐름이 틀렸다고는 볼 수 없을테지만...
너~무 외우다시피해서 ❗공식화하는건 적용이 안된다 => 코드 수정해야함
지금도 인접행렬을 막 만들려고 했음. 이게 다 너무 공식화 해서 그럼 (마찬가지로 visited 라는것도 알고있는 것과 똑같이 할 필요가 없음)
❗인접행렬도 없는게 사실 더 좋음. 이웃한 정보를 쉽게 표현못해서 수동으로 만든거니까
bfs dfs는 늘 "이웃한 정보가 무엇인지를"❗ 생각하는게 가장 중요!
인접행렬을 하나하나 다 만드는 바람에 참조할 필요도 없는걸 참조해서 시간 ㅈㄴ 오래걸림
'''
from collections import deque
import sys

def bfs(node, target, visited):
    queue = deque([node])
    # visited[node] = True
    
    while queue:
        node = queue.popleft()
        if node == target :
            return visited[node]
        # for adj_node in matrix[node]: <- 이렇게 할 필요가 없잖아!
        for adj_node in (node-1, node+1, node*2): # ❗❗
            if 0<=adj_node < MAX and not visited[adj_node] : 
                queue.append(adj_node)
                visited[adj_node] = visited[node] + 1

if __name__ == '__main__':

    now, target = map(int, sys.stdin.readline().split())
    # matrix = [[0,1]]
    # for i in range(1,target*30):
    #     matrix.append([i-1, i+1, i*2]) <- 이렇게 인접행렬을 하나하나 만들려 한 모습
    MAX = 10**5
    visited = [0] * (MAX +1)
    result = bfs(now, target, visited)
    print(result)