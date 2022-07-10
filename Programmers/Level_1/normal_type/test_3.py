def sum_1d_arr(arr1, arr2) :
    result_arr = []
    length = len(arr1)
    for i in range(length) :
        result_arr.append(arr1[i] + arr2[i])
    return result_arr

def solution(arr1, arr2):
    answer = []
    length = len(arr1)
    # print(f'length : {length}')
    for i in range(length) :
        element = sum_1d_arr(arr1[i],arr2[i])
        # print(f'element : {element}')
        answer.append(element)
    return answer

if __name__ == '__main__' :
    arr1 = [[1,2],[2,3]]
    arr2 = [[3,4],[5,6]]
    result = solution(arr1, arr2)
    print(result)