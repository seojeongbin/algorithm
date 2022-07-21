'''
level : silver 2
type : greedy
- 주어진 식에서 괄호를 쳐서 값을 최소로 만들기
- 입력에서 처음과 마지막은 숫자
- 수는 0으로 시작 가능
'''

# - 가 없으면 그냥 그대로 연산
# - 가 나오면 새로운 - 나오기 전까지 항상 괄호
# '55-50+40-36+10-7+10+1+2+3'
# 55 - (50 + 40) - (36 + 10) - (7 + 10...)

formula = input() 
# case 1 : 연산자없이 숫자만 있는경우
if ('-' not in formula) & ('+' not in formula) :
    result = [int(formula)]
# case 2 : + 만 있는경우
elif '-' not in  formula :
    formula_list = list(map(int, formula.split('+')))
    result = formula_list
# case 3 : +, - 둘다 있는경우 : 첫번째꺼 빼고 나머지는 마이너스 적용해서 더하기
else :
    formula_list = list(map(str, formula.split('-')))
    result = []
    for i in range(len(formula_list)) :
        fomula_elem = formula_list[i]
        elem = sum(list(map(int, fomula_elem.split('+'))))
        if i > 0 : elem *= (-1)
        result.append(elem)

print(sum(result))




