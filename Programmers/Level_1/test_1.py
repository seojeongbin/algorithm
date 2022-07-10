a, b = map(int, input().strip().split(' '))
# print(a + b)
for j in range(b) :
    for i in range(a) :
        print('*', end='')
    # print('\n') 이렇게하면 아예 줄이 띄워짐 !
    print('')