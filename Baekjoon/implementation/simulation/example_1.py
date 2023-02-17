'''
implementation.ipynb의 예시문제 복습
- 전체 공간을 매트릭스로 생각, 공간 벗어나는 것도 생각해야
- 현재위치 x,y
- 이동벡터 정의 dx, dy 
- continue 주의
'''

size = 5
move_plan = ['R', 'R', 'R', 'U', 'D', 'D'] 

# L, R, U, D
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

x, y = 1, 1
for plan in move_plan :
    if plan == 'L' :
        if y == 1:
            continue
        x += dx[0]
        y += dy[0]
    elif plan == 'R' :
        if y == size :
            continue
        x += dx[1]
        y += dy[1]
    elif plan == 'U' :
        if x == 1:
            continue
        x += dx[2]
        y += dy[2]
    elif plan == 'D' :
        if x == size :
            continue
        x += dx[3]
        y += dy[3]

print(x, y)