'''
최대공약수, 최소공배수 구하기
'''

def sol1(n,m) : # 최대공약수
    var = 0
    while True :
        var += 1
        if (n%var == 0) & (m%var ==0) :
            result = var
        if var > min(n,m) : break
    return result

def sol2(n,m) : # 최소공배수
    var = sol1(n,m)
    var1 = n//var
    var2 = m//var
    result = var*var1*var2
    return result

def solution(n, m):
    
    result = []
    result.append(sol1(n,m))
    result.append(sol2(n,m))
    return result

if __name__ == '__main__' :
    result = solution(3,12)
    print(result)
    result = solution(2,5)
    print(result)

