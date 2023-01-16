from bisect import bisect_left, bisect_right

def count_within_range(array, value_1, value_2):
    right_index = bisect_right(array, value_2)
    left_index = bisect_left(array, value_1)
    return right_index - left_index

num = int(input())
box = list(map(int, input().split()))
box.sort()

num = int(input())
var = list(map(int, input().split()))

for i in var :
    if count_within_range(box, i, i) > 0 :
        print('1')
    else : 
        print('0')
