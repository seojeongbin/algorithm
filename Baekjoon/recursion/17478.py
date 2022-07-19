'''
- level : silver 4
- type : recursion
    => 재귀란, 함수 내부에서 상황에따라 작동을 다르게하고(특수상황 먼저 정의, 일반적상황 else로 정의), 자기자신을 호출.
<n번째 피보나치 수 구하기>
def fib(n):
    if n<=1 : return n
    elif n==2 : return 1
    else :
        return fib(n-1) + fib(n-2)
'''

### global params
repeat_text = [
        '"재귀함수가 뭔가요?"',
        '"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.',
        '마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.',
        '그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."'
    ] # 반복문구
answer = '라고 답변하였지.'
cnt = 0 # 재귀횟수
bar = '_' # under_bar라고 이름 똑같이 설정하고 *= 이렇게하면 오류난다.

def recursion(iteration, cnt) :
    under_bar = bar * (4 * cnt)
    if iteration == cnt :
        print(under_bar + '"재귀함수가 뭔가요?"')
        print(under_bar + '"재귀함수는 자기 자신을 호출하는 함수라네"')
        print(under_bar+ "라고 답변하였지.")
        return # 종료시킴
    else :
        for text in repeat_text :
            print(under_bar + text)
    cnt += 1
    recursion(iteration, cnt)
    print(under_bar + answer) # 내부 재귀함수 호출 종료 후, 순차적으로 출력되는 문구

if __name__ == "__main__" :
    iteration = int(input())
    print("어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.")
    recursion(iteration, cnt)
