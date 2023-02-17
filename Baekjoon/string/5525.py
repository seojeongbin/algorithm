'''
분류 : 문자열
레벨 : 실버1
문자열 S에 Pn이 몇개 포함되었는가
P1 IOI
p2 IOIOI
p3 IOIOIOI
'''

N = int(input())
M = int(input())
S= input()

Pn = 'O'* (2*N + 1)
Pn = list(Pn) # ❗문자열은 수정이 안되므로 리스트로 변경

for i in range(len(Pn)):
    if i%2 == 0 :
        Pn[i] = 'I' # Pn 생성

# 다시 리스트에서 문자열로 변경
Pn_str = ''
for i in Pn:
    Pn_str += i
Pn = Pn_str

# for문 돌면서 확인
cnt = 0
for i in range(M-len(Pn)+1) :
    if S[i:i+len(Pn)] == Pn : cnt += 1

print(cnt)