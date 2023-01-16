'''
level : silver 2
type : parametric search (이진 탐색 중 특수 유형)
- 최소 N개를 얻을 수 있게 해주는 최대 분등 길이 출력
- 이진 탐색 응용
- 주의 : 기존처럼 start = 0 -> 이렇게 하면 i//mid에서 0될경우 에러나올 수 있음. end 0 이면 mid 0 되기 때문. 그러므로 애초에 start = 1 로 설정해서 mid 0 안노엑 처리
'''

# input
num, N = map(int, input().split())
array = []
for _ in range(num):
    array.append(int(input()))
    
# parametric search
start = 1
end = max(array)

while (start<=end):
    mid = (start + end) // 2
    total = 0
    # 0. 분등 개수 구하기
    for i in array :
        total += (i//mid)
    # 1. 위에서 구한 것을 바탕으로 yes, no 결정 : 더 줄여야 하는가 (왼쪽으로 이동해야 하는가)
    if total < N :
        # 이건 아예 만족하질 않는경우니까 기록할게 없음
        end = mid - 1
    # 2. 위에서 구한 것을 바탕으로 yes, no 결정 : 덜 줄여야 하는가 (오른쪽으로 이동해야 하는가)
    else :
        # 만족하는 경우니까 기록 (=> 이게 loop 돌면서 최적값 산출)
        result = mid
        start = mid + 1
        
print(result)