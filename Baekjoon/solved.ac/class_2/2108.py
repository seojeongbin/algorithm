'''
유형 : 수학, 구현, 정렬
레벨 : 실버3
포인트
- 구현
- 정렬
- 중앙값은 정렬한뒤 가운데있는 값임
- 리스트 컴프리헨션
'''

N = int(input())
numbers = [int(input()) for _ in range(N)]

def mean(numbers):
    result = sum(numbers) / len(numbers)
    return int(round(result, 0))

def median(numbers):
    numbers.sort()
    idx = len(numbers) // 2
    return numbers[idx]

def get_range(numbers):
    return max(numbers) - min(numbers)

def get_most_freq(numbers):
    rank = []
    for number in numbers :
        cnt = numbers.count(number)
        rank.append([cnt, number])
    rank.sort(reverse=True)
    # 여러개인지 확인
    max = rank[0][0]
    # print(f'rank : {rank}, max : {max}')
    if [i[0] for i in rank].count(max) == 1:
        return rank[0][1]
    else :
        array = [i[1] for i in rank if i[0] == max]
        array = list(set(array))
        array.sort()
        return array[1]
        

if __name__ == '__main__' :
    print(mean(numbers))
    print(median(numbers))
    print(get_most_freq(numbers))
    print(get_range(numbers))