'''
type : 2d array, 구현 / silver 5
전체 100 * 100 영역
10 * 10 의 색종이를 붙일경우, 중복영역 면접 넓이 합
입력 : 색종이의 좌측하단 좌표
❗ 이중 매트릭스 쓸때, 값을 초기설정 후 변경해야하는경우 깊은복사 얕은복사에 주의한다!!!!
'''
size = 100
# board = [[0]*100]*100 => ❗ 이렇게하면 하나 바꾸고 싶을때 전체 다 바뀌어버림!! [][]로 값 변경이 안됨
board = [[0]*size for _ in range(size)]

N = int(input())
for _ in range(N):
    x, y = map(int, input().split())
    for i in range(x, x+10):
        for j in range(y, y+10):
            board[i][j] = 1

sum = 0
for i in range(100):
    for j in range(100):
        sum += board[i][j]
        
print(sum)