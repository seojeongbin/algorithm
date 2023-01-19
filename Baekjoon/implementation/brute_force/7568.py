'''
level : silver 5
type : brute force
- 입력받은 인원들의 덩치 등수 정하기
- 등수 : 자기보다 덩치 큰 사람 수 + 1
'''

N = int(input())
weights = []
heights = []
for _ in range(N):
    w, h = map(int, input(). split())
    weights.append(w)
    heights.append(h)
    
for i in range(N):
    rank = 1
    # 키도 크고 & 몸무게도 크면 += 1
    for j in range(N):
        if j == i :
            continue 
        if (weights[j] > weights[i]) & (heights[j] > heights[i]):
            rank += 1
    print(rank, end= ' ')
                
'''
코테
- 최대한 간단한, 제일 쉬운 방법으로 생각
- 머리로만 하지말고 도식화 하는 습관 (그림으로 라든지, 글로라든지)
'''
            

