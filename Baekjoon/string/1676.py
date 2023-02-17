# N!에서 뒤에서부터 처음 0이 아닌 숫자가 나올 때까지 0의 개수를 구하는 프로그램을 작성하시오.
# 유형 : 수학 & 문자열

N = int(input())

result = 1
for i in range(1,N+1):
    result *= i
result = str(result)
result = result[::-1] # 이게 주요했다

cnt = 0
for i in result :
    if i != '0' :
        break
    else :
        cnt += 1
    
print(cnt)

# 문제다시 읽업굊 ㅗㄱ므 다름