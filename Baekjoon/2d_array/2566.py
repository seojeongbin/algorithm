import sys
input = sys.stdin.readline
board = []
for _ in range(9):
    board.append(list(map(int, input().split())))

max = 0
box = []    
for i in range(9):
    for j in range(9):
        if board[i][j] >= max :
            max = board[i][j]
            box.append([i+1,j+1])
            
print(max)
print(*box[-1])