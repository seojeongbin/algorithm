'''
- python으로 stack 구현하기 : 그냥 리스트로 append(push), pop(pop) 하는거임 !!
- 다만 실제 스택과 달리 인덱스로도 접근이 가능함 파이썬은..
'''

iterations_num = int(input())
stack = []
for _ in range(iterations_num) :
    number = int(input())
    if number != 0 :
        stack.append(number)
    else :
        stack.pop()
result = sum(stack)
print(result)