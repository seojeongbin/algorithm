'''
level : bronze 2
type : brute force
- N개의 입력 중, 3개의 합이 M을 넘지 않으면서 최대한 가까운 카드 3장의 합
- 완전 탐색의 경우 전체에서 3개씩 묶은 모든 경우를 탐색한다 이런게 많아서 수학때 배웠던 순열 조합 이런걸 많이 쓰게됨
'''
from itertools import combinations # 조합

pick_num = 3
N, M = map(int, input().split())
# N, M = int(input()).split()

# elem_box = [int(input()) for _ in range(N)]
elem_box = list(map(int, input().split()))
combinations = list(combinations(elem_box, pick_num))
sum_list = [sum(combination) for combination in combinations if sum(combination) <= M]
sum_list.sort(reverse=True)

print(sum_list[0])