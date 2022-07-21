'''
level : silver 4
type : greedy
N = 전체인원, P_i = 각 사람 인출소요시간
* [각 사람 필요시간 = 전체 앞 사람들의 인출시간 + 본인인출시간]
* 어떻게 줄 서느냐에 따라 전체 소요시간이 달라짐
* 최소 소요시간 구하기
'''

# greedy : 매 순간 최적 상황을 선택
# 제일 적게 걸리는 순으로 진행하면됨 (오름차순의 로직이 맞다는 철저한 가정하에 하는것임. 그게 아니라면 완전탐색)

N = int(input())
people = list(map(int, input().split()))
people.sort()
spend_time = [people[:i+1] for i in range(N)]
result = sum([sum(time) for time in spend_time])
print(result)
