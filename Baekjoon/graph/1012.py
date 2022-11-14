'''
level : silver 2
type : dfs
<문제 설명>
- 입력) 가로 길이, 세로 길이, 배추 개수
- 출력) 군집 수
★ 2667처럼 상황이 틀인경우 (입력 주의)
'''
import sys
sys.setrecursionlimit(10**9)  

## 2. 틀 문제에 이용되는 dfs
def dfs(x, y):
    if x <= -1 or x >= h or y <= -1 or y >= w :
        return False
    if graph[x][y] == 1 :
        graph[x][y] = 0
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False

## 1. 입력
num_tc = int(sys.stdin.readline().rstrip())
for _ in range(num_tc) :
    tmpL = list(map(int,sys.stdin.readline().split()))
    w, h, n = tmpL[0], tmpL[1], tmpL[2]
    graph = [[0]*w for _ in range(h)] # 2차 리스트 주의 ★ 문제에 맞게 표현
    
    for _ in range(n):
        tmpL = list(map(int,sys.stdin.readline().split()))
        x, y = tmpL[0], tmpL[1]
        graph[y][x] = 1 # 문제 구조 생각해보면 이렇게 하는게 맞음

    ## 3. 출력
    result = 0
    for x in range(h):
        for y in range(w): # ★ h,w 주의 w,h 아님
            if dfs(x, y) == True:
                result += 1
    print(result)
    result = 0 # ★ 초기화