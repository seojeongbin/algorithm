'''
level : silver 1
type : dfs
<문제 설명>
- 입력) 지도 크기, 줄별 정보(인접 행렬)
- 출력) 군집 수, 군집 별 원소 수
★ graph가 인접행렬이 아니라 틀인경우 함수를 달리짜야한단게 포인트 (dfs 연습문제 형태임)
'''
import sys
sys.setrecursionlimit(10**9)  

## 1. 입력
N= int(input())
graph = []
for _ in range(N):
    graph.append(list(map(int, input())))

## 2. dfs 함수
cnt = 0
def dfs(x, y):
    global cnt
    # 이 부분 필수임 (10번정도 이 부분 해당하게 됨)
    # 예를들어 첫 시작점에서 x-1, y는 없는 부분에 해당하게 됨
    if x < 0 or x >= N or y < 0 or y >= N:
        return False
    
    # '처음' 으로 방문안한곳을 방문하는거라면 방문처리
    if graph[x][y] == 1 :
        graph[x][y] = 0
        cnt += 1
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True # 처음 방문한게 맞으니까 return True # ★ return True, cnt 이렇게 안해도 전역변수라 알아서 되는듯..?
    return False

## 3. 출력
if __name__ == "__main__" :
    result = 0
    cnt_box = []
    for x in range(N)        :
        for y in range(N) :
            # 현재 위치에서 dfs가 처음으로 수행된 것이라면
            if dfs(x, y) == True : 
                result += 1
                cnt_box.append(cnt)
                cnt = 0 # ★★★ cnt는 군집 별 원소개수니까 다시 초기화해줘야 함 전역으로 쓰고 있어서!!
    cnt_box.sort()
    print(result)
    for cnt in cnt_box :
        print(cnt)