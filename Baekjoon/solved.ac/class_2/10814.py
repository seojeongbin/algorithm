# 정렬
N = int(input())
# ages = []
# names = []
# orders = []
dict = {}
array = []
for idx in range(N):
    age, name = input().split()
    age = int(age)
    array.append([age, idx, name]) # 이 순서로 정렬해준다
array.sort()
for i in array :
    print(f'{i[0]} {i[2]}')

# 정렬에 조건 두가지 붙은경우 sort에서 한번에 될수있음을 생각
# array.append([age, idx, name]) # 이 순서로 정렬해준다