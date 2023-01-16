'''
level : silver 2
type : parametric search (이진 탐색 중 특수 유형)
ipynb 예제와 거~의 똑같은데 시간초과가 이슈. if break 추가하면 되었음..
참고
- break : (가장 1단계 수준만) loop 전체를 부수는 느낌
- continue : 해당 case만 벗어나는 느낌
'''

# input
num, target_length = map(int, input().split())
array = list(map(int, input().split()))

start = 0
end = max(array)

# search
while (start <= end) :
    mid = (start + end)//2
    total = 0
    # 1. 꼬다리 합 구하기 
    for tree in array :
        if tree - mid > 0 : # 큰 나무만 잘리니까!! 이거 다 하면 length가 음수나올 수 있으니까
            length = tree - mid
            total += length
        if total > target_length : # ❗ 절단할 나무 추가하는 도중, 이미 target을 넘었다면 그만추가한다
            break
    # 2. yes or no 판단 : 부족할경우 (더 잘라본다)
    if total < target_length :
        end = mid - 1
    # 3. yes or no 판단 : 부족하지 않을 경우 (덜 잘라본다)
    else :
        result = mid
        start = mid + 1
        
print(result)
    