N = int(input())
array = []
for _ in range(N):
    x, y = map(int, input().split())
    array.append([y, x])
array.sort()

for var in array :
    print(f'{var[1]} {var[0]}')