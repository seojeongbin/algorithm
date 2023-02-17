'''
- 정렬
- N개 만큼 단어 입력을 받음
- 1)길이가 짧은 순서대로 2) 길이 같을경우 사전 순으로
- 중복된 단어는 하나만 취급. 이 상태로 정렬시키기
'''

import sys

n = int(sys.stdin.readline())
words = []

for _ in range(n):
    words.append(sys.stdin.readline().strip())
words = set(words)
words = list(words)
words.sort()
words.sort(key = len)

for word in words:
    print(word)

# 밑에는 똑같은 과정임... 삽질
# len_dict = {} # 완전히 활용을 못하고 좀 아이디어틱 하게 해결하게 됨..
# for word in words :
#     key = word
#     value = len(word)
#     len_dict[key] = value

# values = []
# for value in list(len_dict.values()) :
#     values.append(value)
    
# values.sort()
# words.sort()

# for value in set(values) :
#     for word in words :
#         if value == len(word):
#             print(word)
            