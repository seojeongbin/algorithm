def solution(arr):
    sum = 0
    for element in arr :
        sum += element
    result = sum / len(arr)
    return result

# !!! 리스트 원소 다 더할때는 그냥 sum(list_name) 이렇게 하면됨!!