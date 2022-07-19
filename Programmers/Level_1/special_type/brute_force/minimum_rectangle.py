'''
완전탐색 (brute force)
- 말그대로 모든 경우를 다 체크하는 방식임 
- for while 등으로도 할 수 있지만 재귀, dfs, bfs, 특히 순열&조합 등 이거까지 알아야함
- 이 문제로 완전탐색 맛만보고 이후 백준에서 해당 유형들 심도있게 공부필요
'''

'''
level : 1
type : brute force
title : minimum rectangle
refer : https://school.programmers.co.kr/learn/courses/30/lessons/86491
description :
- 방향도 돌릴 수 있음을 감안할 때, 최소 크기를 return
- 최소 크기는 가로 * 세로 로 구한다
flow
1. 가로하고 세로중에 가장 큰 값을 고른다.
2. 가장 큰 값이 속한 팀(예를 들어 가로)이 아닌 팀에서 방향을 바꾸어 가며 답을 구한다
'''


def solution(card_list) :
    # step1 : 가장 큰 값 고르기
    width = []
    height = []
    for card in card_list :
        width.append(card[0])
        height.append(card[1])
    w_max = 0
    w_max_idx = 0
    h_max = 0
    h_max_idx = 0
    for idx, (w, h) in enumerate(zip(width, height)) : # zip, enumerate 같이 사용 가능
        if w>w_max :
            w_max = w
            w_max_idx = idx
        if h>h_max :
            h_max = h
            h_max_idx = idx
    result = w_max * h_max # 초기 result 설정.
    
    # step2 : result 이제 계속 갱신해보기
    if w_max >= h_max :
        # w_max_idx를 제외한 idx들에서, 가로와 세로를 한번씩 바꾸면서, 크기 작아지는지 체크
        for idx, card in enumerate(card_list) :
            if idx != w_max_idx :
                # height_new = height => 이렇게하면 영향준다!!!!!!!!!
                height_new = height.copy()
                height_new[idx] = width[idx]
                result_new = w_max * max(height_new)
                if result_new < result :
                    result = result_new
                    # print(f'w_max : {w_max}, height_new : {height_new}, max(width_new) : {max(height_new)}') 
    else :
        for idx, card in enumerate(card_list) :
            if idx != h_max_idx :
                width_new = width.copy() # 이거안하면 원본에도 영향준다!!!!
                width_new[idx] = height[idx]
                result_new = h_max * max(width_new)
                if result_new < result :
                    result = result_new
                    # print(f'h_max : {h_max}, width_new : {width_new},, max(width_new) : {max(width_new)}')       
    return result


if __name__ == '__main__' :
    # sizes = [[60, 50], [30, 70], [60, 30], [80, 40]]	
    # result = solution(sizes)
    # print(f'result : {result}') => 이거는 tc 통과
    sizes = [[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]	
    result = solution(sizes)
    print(f'result : {result}')
    sizes = [[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]
    result = solution(sizes)
    print(f'result : {result}')

'''
일부 tc만 통과하고 틀림.
=> 가로, 세로 중 큰 값을 모두 가로로 두고, 작은값은 세로로 취급
=> 가로/세로 가장 큰 값으로 만든 사각형의 넓이가 답이 됨.
'''

def solution(sizes):
    # https://leeiopd.tistory.com/entry/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-level1-%EC%B5%9C%EC%86%8C%EC%A7%81%EC%82%AC%EA%B0%81%ED%98%95-Python-%ED%8C%8C%EC%9D%B4%EC%8D%AC?category=944401?category=944401
    pass