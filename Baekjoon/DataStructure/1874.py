'''
platform : backjoon
type : stack
level : silver 2
'''

iterations = int(input())
stack = []
result = []
idx = 1
for _ in range(iterations) :
    # print(f'stack : {stack} \t result : {result} \t idx : {idx}')
    input_num = int(input())
    # if idx <= input_num :
    while idx <= input_num :
        stack.append(idx)
        idx += 1
        print('+')
    # else : => 이 로직이 틀린듯
    #     while idx > input_num :
    #         result.append(stack.pop())
    #         idx -= 1
    #     idx = result[0] + 1
    if stack[-1] == input_num :
        # result.append(stack.pop())
        stack.pop()
        print('-')
    else :
        print('NO')
        break

# print(result)