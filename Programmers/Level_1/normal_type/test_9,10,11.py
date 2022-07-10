def solution(num):
    if num % 2 == 0 :
        return 'Even'
    else :
        return 'Odd'

def solution(arr):
    if len(arr) == 1: return [-1]
    else :
        Min = min(arr)
        arr.remove(Min)
        return arr

def solution(n):
    
    var = 0
    while True :
        var += 1
        if var ** 2 == n : 
            return (var+1)**2
        elif var > n :
            return -1