
def solution(number):
    
    SUM = 0
    for i in str(number) :
        SUM += int(i)

    if number % SUM == 0 :
        result = True
    else :
        result = False
    return result

if __name__ == '__main__' :
    numbers = [10,12,11,13]
    for number in numbers : 	
        result = solution(number)
        print(result)
