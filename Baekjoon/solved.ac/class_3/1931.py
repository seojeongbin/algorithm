'''
분류 : 정렬, 그리디
타입 : 실버1
최대 가능 회의 개수
'''

N = int(input())
times = []
for _ in range(N):
    start, end = map(int, input().split())
    # cost = end - start
    times.append([end, start])
    
times.sort()

cnt = 0
prior_start, prior_end = 0,0
for time in times :
    start = time[1]
    end = time[0]
    
    if start >= prior_end :
        cnt += 1
        prior_start = start
        prior_end = end

print(cnt)