'''
level : silver 4
type : greedy
<about greedy>
그리디 관련 유튜브 강의링크 : https://youtu.be/2zjoKjt97vQ
그 순간에서 최적의 방법을 선택해나가는 방법
=> 정당성에 대한 고려가 필요함
1. 선택지 중에 최적의 선택지를 하게 로직 설정
2. 고른 최적의 선택이 다른것보다 우등한 이유가 무엇인지
=> 예를들어 거스름돈 동전 수 최소하기위해 500원 > 100원 우월이유 명확해야
=> 위의 예시에서는 500원이 100원의 배수이기 때문임!! 400원 vs 300원은 무지성 400을 채택할 수 없음
'''

# target을 만들기위해 coin_num 종류 중 동전 개수 최소값
coin_num, target = input().split()
coin_num, target = int(coin_num), int(target)
coin_list = [int(input()) for _ in range(coin_num)] # 이렇게 리스트 컴프리헨션 앞으로 적극 이용하기
coin_list.sort(reverse=True)

cnt = 0
for coin in coin_list :
    quota = target // coin
    cnt += quota
    target -= quota * coin

print(cnt)