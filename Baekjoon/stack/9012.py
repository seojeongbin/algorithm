# 괄호 정상인지 판단하는건 'stack의 대표예시' 라서 어렵지 않게 풀었지만,
# stack의 사용상황을 판단하는게 포인트임! 

def isPS(string):
    stack = []
    for elem in string :
        if elem == '(' :
            stack.append(elem)
        else :
            if len(stack) != 0 :
                stack.pop()
            else :
                return False
    if len(stack) == 0 :
        return True
    else :
        return False
        
iterations_num = int(input())
stack = []
for _ in range(iterations_num) :
    string = input()
    if isPS(string) :
        print('YES')
    else :
        print('NO')