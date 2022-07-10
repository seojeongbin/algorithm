
def solution(phone_number):
    
    criteria = 4
    length = len(phone_number)
    result = ''

    # condition = True 
    for idx, number in enumerate(phone_number) :
        if length - idx <= criteria :
            number = '*'
        else :
            number = number
        # result.append(number) !!! 리스트 []와 다르게 빈 문자열 ''경우 append 불가 => += 이런식으로 해야함
        result += number
    return result

if __name__ == '__main__' :
    phone_number = "01033334444"	
    result = solution(phone_number)
    print(result)

'''
총 11자리
0 1 2 3 4 5 6 7 8 9 10
4이하로 차이나게 됨 
'''