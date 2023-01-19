'''
level : bronze 2
type : brute force
- 256 = 245 + 2 + 4 + 5 : 245는 256의 생성자
- 자연수 N 주어졌을 때, 그 수에 대한 최소 생성자 구하기 (없을 경우 0출력)
'''

N = int(input())

for decisior in range(1, N+1):
    
    total = 0
    for i in str(decisior) :
        total += int(i)
    total += decisior
    
    if total == N :
        print(decisior)
        break
        
    if decisior == N :
        print(0)
        
'''
완전 탐색임은 알았지만
for문 쓸 생각은 못했음
❗ 완전 탐색일 땐 => "for문"으로 무지성 1씩 가능한 전체범위로 다 키워본다 생각!!
완전 탐색이란게 말 그대로 전체 영역 본다거니까
'''