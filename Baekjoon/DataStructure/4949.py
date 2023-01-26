import sys
input = sys.stdin.readline

def isTrue(string):
    stack = []
    box = ['(','[',')',']']

    for elem in string :
        if elem not in box :
            continue

        if (elem == '(') or (elem == '[') :
            stack.append(elem)
        # else :

            '''
            <잘못된 코드1>
            if (elem == ')') and (stack.count('(') == 0 ): 
                return False
            if (elem == ']') and (stack.count('[') == 0 ):
                return False
            else :
                stack.pop()
            => 괄호간의 순서를 고려하지 않음
            => [) (] 이런경우를 못잡기 때문에 순서도 중요!
            '''

            '''
            <잘못된 코드2>
            if (stack) and (elem == ')') and (stack[-1] == '(') : # stack[-1]은 empty 경우 error 이므로 앞에 stack 조건을 추가
                stack.pop()
            if (stack) and (elem == ']') and (stack[-1] == '[') :
                stack.pop()   
            else :
                print(f'here elem : {elem} \t stack : {stack}, stack[-1] : {stack[-1]}')
                return False
            # => ()[] 이렇게 안끝났는데도 empty 여서 return false 될 수 있음
            # => 가정문에서 3중조건은 나눠서 작성하기..
            '''
            
        elif elem == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                return False
        elif elem == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                return False

    if len(stack) == 0 :
        return True
    else :
        return False
    


while True :
    
    # string = input()
    string = input().rstrip()

    if string == "." :
        break

    if isTrue(string):
        print('yes')
    else :
        print('no') 