'''
- level : gold 4 (이 문제는 추후 복습 좀 하기 당장은 꽤나 어려웠다.)
- origin / refer : https://www.acmicpc.net/problem/2110 / https://my-coding-notes.tistory.com/119
- type : parametric search (이진 탐색 중 특수 유형)
- 집 좌표의 범위 굉장히 넓음 => 이진 탐색 떠올릴 수 있음
- 기존처럼 target 값이 있는 상황에서 이걸 넘어야 되는게 아님. "어느 집에다가 공유기 설치할 것인가"
- 공유기 개수가 무한정 많을 수 있다는 것도 고려해야.
- ❗ 집 좌표가 그러니 이진 탐색 대상 아닐까(X) => 공유기 설치할 거리 사이를 기준으로 이진탐색 하는 것임!!
- ❗ 현재 집에서 다음 집 까지의 거리가 mid를 초과해야지 공유기 설치 가능! (언제나 이진탐색의 아이디어로 구해내는 건 ❗mid다!!!)
- ❗ 이것도 결국은 기존 3가지 구조랑 같다!!
'''

### input

import sys
input = sys.stdin.readline # ❗ 백준할때 input 받을때 이거 먼저 호출하기
num, target_num = map(int, input().split())
array = []
for _ in range(num) :
    array.append(int(input()))
array.sort()
    
### search

# 공유기 사이 거리를 이분 탐색으로 결정 한단 것을 명심 : start를 공유기 사이 최소 거리, end를 공유기 사이 최대 거리
start = 1 # start = 0[X] => 공유기 사이 존재할 수 있는 최소거리가 1이니까
end = max(array) - min(array) # end = max(array)[X] => 공유기는 집에다가 설치하는건데, 최대 거리는 집간거리가 젤 먼경우니까

while (start<=end):
    mid = (start + end) // 2
    current = array[0]
    cnt = 1 # 공유기 개수
    
    for i in range(1, len(array)):
        if array[i] >= current + mid :
            current = array[i]
            cnt += 1
    
    if cnt >= target_num : # 사이 거리 넓히기
        start = mid + 1
        result = mid 
        
    else : # 사이 거리 좁히기
        end = mid - 1

print(result)