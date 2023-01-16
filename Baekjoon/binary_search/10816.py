from bisect import bisect_left, bisect_right

def count_within_range(array, value1, value2):
    right_index = bisect_right(array, value2)
    left_index = bisect_left(array, value1)
    return right_index - left_index

num = int(input())
box = list(map(int, input().split()))
box.sort()

num = int(input())
vars = list(map(int, input().split()))

for var in vars :
    cnt = count_within_range(box, var, var)
    print(cnt, end = ' ')
    
    