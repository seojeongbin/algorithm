'''
level : silver 5
type : brute force
- 종말의 숫자 : 수에 6이 적어도 3개이상 연속으로 들어가는 수
- 제일 작은 종말의 수 : 666 -> 1666 -> 2666
- N번째 작은 종말의 수 구하기
- ❗ 완전탐색을 떠올리는게 중요했던 문제!! 떠올렸다면 시원하게 for !!
'''

N = int(input())

def is_true(number):
    if '666' in str(number):
        return True

answer = 0
cnt = 0
while True :
    answer += 1
    if is_true(answer) :
        cnt += 1
    if cnt == N :
        print(answer)
        break
    