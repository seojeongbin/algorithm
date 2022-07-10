'''
문제명 : 콜라츠 추측
'''

def solution(number):
    
    if number ==1 : return 0
    cnt = 0
    criteria = 1
    while number != criteria :
        if cnt == 500 : return -1
        if number % 2 == 0:
            number /= 2
        else :
            number *= 3
            number += 1
        cnt += 1
    return cnt

if __name__ == '__main__' :
    numbers = [6,16,626331]
    for number in numbers : 	
        result = solution(number)
        print(result)
