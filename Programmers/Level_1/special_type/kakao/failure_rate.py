'''
level : 1
type : 2019 KAKAO BLIND RECRUITMENT
title : failure rate
refer : https://school.programmers.co.kr/learn/courses/30/lessons/42889
description :
- N = 스테이지 수
- stages = 멈춰있는 스테이지 번호
- result = 실패율이 높은 스테이지 내림차순 (머문사람 / 도달한사람)
flow
1. 스테이지 별 도달한사람과 머물고 있는 사람을 딕셔너리
2. 스테이지 별 실패율을 딕셔너리로 저장
3. 실패율(value)을 내림차순으로 갖는 스테이지 번호(key)를 리스트로 출력 
'''

'''
1. 딕셔너리 활용 가능성을 항상 이제 염두하기
2. 나눌때는 0 주의 & 런타임에러 뜰경우 0으로 나누진 않았는가 체크
3. 리스트 한줄표현!! & lamgda 사용법 숙지하기
    - 리스트 한 줄 표현 : 빈 리스트에 append 하는경우
    - lambda => lambda 입력변수 : 표현식(&조건식) => lambda라는건 표현식이나 조건식을 수행하는 '함수객체'인것임! 
    - map => map(함수식, 리스트)
'''

def solution(n, stages) :
    # 1. 스테이지 n개 별로 도달한 사람을 구한다
    dict = {}
    for i in range(n) :
        i += 1
        stage_now = stages.count(i)
        # 2. stages 리스트에서 i 이상인 수를 카운트 
        # count = sum(map(lambda x : x >= i, stages)) => 시간초과
        count = len([x for x in stages if x>=i]) # 이렇게 lambda 사용하지않고 한줄로도 표현가능..
        if count == 0 :
            dict[i] = 0
        else :
            dict[i] = stage_now / count
    # 3. 실패율(value) 기준 내림차순
    sorted_dict = sorted(dict.items(), key = lambda item: item[1], reverse = True)
    # 4. key를 리스트로 출력
    result = []
    for i in range(n) :
        result.append(sorted_dict[i][0])
    return result


if __name__ == '__main__' :
    
    n = 5
    stages = [2, 1, 2, 6, 2, 4, 3, 3]	
    result = solution(n, stages)
    print(f'result : {result}\n')
    n = 4
    stages = [4, 4, 4, 4, 4]	
    result = solution(n, stages)    
    print(f'result : {result}\n')

