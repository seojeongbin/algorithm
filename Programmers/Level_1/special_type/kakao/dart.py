'''
level : 1
type : kakao
title : dart game
refer : https://school.programmers.co.kr/learn/courses/30/lessons/17682
description :
single / double / triple 영역에따라 **n
스타상 * => 해당점수, 직전점수 *2
아차상 # => 해당점수 * (-1)
- 점수는 0~10 int
- 스타상, 아차상은 둘 중 하나만 존재가능, 없을수도 있음
- S, D, T 영역은 꼭 하나씩은 존재함
ex) 
1S2D*3T => 1S, 2D*, 3T
1S*2T*3S => 1S*, 2T*, 3S => 4 + 16 + 3	
'''

'''
프로그래머스 사이트에서 다른사람들 풀이보면서 다시 복습하기!!!
'''

def solution(string) :

    string = string.replace('10','!')
    # 10을 처리해주기 위해!!!! << 이 부분만 빼고 tc 모두 통과. 이 부분만 구글링으로 아이디어 얻음.
    # 형태때문에 특수하게 처리하기 어려운 경우 형태를 원하는대로 바꿔줄 수 있음! 
    check_type = ['S', 'D', 'T']
    check_symbol = ['*', '#']
    check_int = ['!']
    for i in range(11) :
        check_int.append(str(i))

    score_box = [0] * 3
    idx_pointer = -1 # 0부터 시작하도록 맞춰주기 위해
    for elem in string :
        if elem in check_int :
            idx_pointer += 1
            if elem == '!' : elem = 10
            score_box[idx_pointer] = int(elem)
        if elem in check_type :
            if elem == 'S' : score_box[idx_pointer] **= 1
            if elem == 'D' : score_box[idx_pointer] **= 2
            if elem == 'T' : score_box[idx_pointer] **= 3
        if elem in check_symbol :
            if elem == '#' : score_box[idx_pointer] *= (-1)
            if elem == '*' :
                score_box[idx_pointer] *= 2
                if idx_pointer > 0 :
                    score_box[idx_pointer-1] *= 2
        
    result = sum(score_box)
    return result

if __name__ == '__main__' :
    
    dart_strings = ['1S2D*3T', '1S*2T*3S', '1D#2S*3S' ,'1D2S#10S'] 
    for dart_string in dart_strings :
        result = solution(dart_string)
        print(result)
