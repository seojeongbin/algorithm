'''
level : 1
type : kakao
title : secret map
refer : https://school.programmers.co.kr/learn/courses/30/lessons/17681
description :
- 지도 하나는 한변이 n(1~16 int)인 정사각형. 빈칸(''), 벽(#) 으로 구성됨
- 지도 두개 겹쳐서 전체 지도. 하나라도 벽이면 벽. 모두 공백이여야 공백.
- 지도의 빈칸, 벽 정보는 0(공백) , 1(벽)으로 암호호됨.
flow
1. 입력받은 arr 두개를 binary로 변경한다 : 자릿수 유지 주의
2. 변경된 arr를 합연산하는데 이 때 1이 넘어가면 0으로 변경 
3. 다시 문자로 변경
'''

def decimal_to_binary(n, criteria): # 이 부분 고수들 어떻게 했는지 체크
    result = "{0:b}".format(int(n)) # 구글링으로 얻은 코드는 여기까지. 밑에는 5줄 채울려고 추가한 내용.(이거는 zfill 쓰면된다!!!)
    if len(result) != criteria :
        num_added = criteria - len(result)
        result = '0'*num_added + result
    return result # type : 'str'임

def solution(n, arr1, arr2) :

    arr1_binary = []
    arr2_binary = []
    for elem1 in arr1 : # for 두개로 각각 적용함 : 이 부분 좀 더 간소화 할 수 있는지 체크
        elem1_binary = decimal_to_binary(elem1, n)
        arr1_binary.append(elem1_binary)
    for elem2 in arr2 :
        elem2_binary = decimal_to_binary(elem2, n)
        arr2_binary.append(elem2_binary)
    print(f'arr1_binary : {arr1_binary}')
    print(f'arr2_binary : {arr2_binary}')
    map_array = []
    for i in range(n) :
        map_elem = int(arr1_binary[i]) + int(arr2_binary[i]) # 12121 : int
        map_elem_str = str(map_elem)
        map_elem_str = map_elem_str.replace('2','1') # !!replace 적극활용하기!!! : '12121' => '11111' 이런식으로 문자열 내부에도 사용가능.
        if len(map_elem_str) != n :
            num_added = n - len(map_elem_str)
            map_elem_str = '0'*num_added + map_elem_str
        map_array.append(map_elem_str)
    print(f'arr3_binary : {map_array}')
    result = []
    for map_elem in map_array :
        map_elem = map_elem.replace('1','#')
        map_elem = map_elem.replace('0',' ')
        result.append(map_elem)
    return result



if __name__ == '__main__' :
    
    n = 5
    arr1 = 	[9, 20, 28, 18, 11]
    arr2 = [30, 1, 21, 17, 28]
    result = solution(n, arr1, arr2)
    print(f'result : {result}')
    # ["#####","# # #", "### #", "# ##", "#####"]
    # 11111, 10101, 11101, 10011, 11111

    n = 6
    arr1 = 	[46, 33, 33, 22, 31, 50]
    arr2 = [27, 56, 19, 14, 14, 10]
    result = solution(n, arr1, arr2)
    print(f'result : {result}')
    # ["######", "### #", "## ##", " #### ", " #####", "### # "]


'''
flow 변경사항
1. bin, zfill(rjust도 가능)
2. 이게 곧 비트연산의 or 연산과 같음
+ replace 애용
'''

def solution(n, arr1, arr2):
    answer = []
    for i,j in zip(arr1,arr2):
        a12 = str(bin(i|j)[2:])
        a12=a12.zfill(n)
        a12=a12.replace('1','#')
        a12=a12.replace('0',' ')
        answer.append(a12)
    return answer