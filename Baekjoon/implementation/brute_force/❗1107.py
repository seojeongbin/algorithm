'''
*** 이거는 코테시즌 다가올때 다시 풀어보기. 완전 탐색 떠올리는 것도 중요하고 짜는것도 중요했다.
유형 : 완전탐색
레벨 : 골드 5
- 현재 보고 있는 채널 100
- 이동하고자 하는 채널 N
- 고장난 버튼 수 M
- 고장난 버튼 목록
=> 최소 몇 번 눌러야 하는가
'''

now = '100'
whole_range = 500000
target = input()
M = int(input())
disabled = list(map(str, input().split()))
abled = list(set([str(i) for i in range(10)]) - set(disabled))

### 1. 구조적으로 늘 분류!해서 접근하기
# (1) only shift 로 init
answer = abs(int(now) - int(target))

### 2. 완전탐색으로 풀기로 한 경우 진짜 아싸리 화끈하게 가야함 => 문제 제공 범위를 for로 다 봐버린단 생각 ㄹㅇ
### 어디채널에서 해야할지를 정하는 거임. 완전탐색으로.
# (2) manual + shift 방법으로 answer 갱신
for channel in range(whole_range*2+1):
    # 한번에 눌러서 해결할 수 있는 채널들을 탐색
    for number in str(channel):
        # 하나라도 없는 경우 다음 채널로 넘어감
        if number in disabled :
            break
    # for - else 는 break로 안부서진 경우 의미함 (없어도 되긴 하는데 가독성땜에 쓰는듯)
    else :
        # manual + shift 갱신
        answer = min(answer, len(str(channel)) + abs(int(channel) - int(target)))

print(answer)        


### 내가 하려했던 코드
# # 몇번째짜리까지 원큐에 되는가
# def check_channel(target, abled):
#     cnt = 0
#     length = len(target)     
#     for i in range(length) :
#         if target[i] in abled :
#             cnt += 1
#     return cnt

# cnt = check_channel(target, abled) # 3

# # target[cnt] # 이 값과 가장 가까운 값의 차이를 구해서 쉬프트 더하려고 했음
# target = int(target[cnt])
# min = 100
# for i in abled :    
#     diff = abs(int(i) - target)
#     if diff <= min :
#         min = diff
# result = cnt + min + 1
# print(result)