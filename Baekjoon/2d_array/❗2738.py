'''
* ❗ 브론즈 5지만 나에게 중요한 문제!!
입력
[[1,1,1],[2,2,2],[0,1,0]]
[[0,1,0],[3,3,3],[5,5,100]]
출력
[[4,4,4],[6,6,6],[5,6,100]]
'''

N, M = map(int, input().split())
matrix_A = []
matrix_B = []

for _ in range (N):
    array = list(map(int, input().split())) # M개 만큼의 원소 입력받음
    matrix_A.append(array)
    
for _ in range (N):
    array = list(map(int, input().split()))
    matrix_B.append(array)

# 방법 1 : 리스트 컴프리헨션과 zip
# append는 무조건 시도해본다 생각! 그 후 변경 => 리스트 컴프리헨션은 최대한 사용하는 버릇들이는게, 생각의 확장성에 좋음
for array_A, array_B in zip(matrix_A, matrix_B):
    array_result = [A + B for A,B in zip(array_A, array_B)]
    print(*array_result)

# 방법 2 : 매트릭스 형태 만들어놓은 상태에서 [][] 이중 인덱스로 접근하기
for i in range(N):
    for j in range(M):
        matrix_A[i][j] += matrix_B[i][j]
for array in matrix_A :
    print(*array)