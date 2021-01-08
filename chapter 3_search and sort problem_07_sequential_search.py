#chapter 3_search and sort
#problem_07_sequential_search

# 순차 탐색
def search_list(a,x):
    """
    for문 활용한 리스트 위치 반환 함수
    입력 : 숫자열 list, target integer
    출력 : 숫자 index
    """
    n = len(a)         # 리스트 입력 크기 n
    for i in range(n): # 리스트 a 원소를 차례로
        if x == a[i]:  # x값과 대조
            return i   # 일치시 위치 반환
    return -1          # 존재하지 않을시 -1 반환

# exercise 7-1
# search_every
def search_every(a,x):
    """
    for문 활용한 리스트 반환 함수
    입력 : 숫자열 list, target integer
    출력 : index list of target integer 
    """
    ans = []                # 정답 리스트 초기화
    for i in range(len(a)): # 리스트 a 원소를 차례로
        if x == a[i]:       # x값과 대조
            ans.append(i)   # 일치시 ans 리스트에 삽입
    return ans              # 리스트 반환

# exercise 7-2
# O(n)

# exercise 7-3
# find_student
def find_student(n,a,b):
    for i in range(len(a)):
        if n == a[i]:
            return b[i]
    return "?"

# sol using zip
def find_student(n,a,b):
    temp = zip(a,b)
    for ele in temp:
        if ele[0] == n:
            return ele[1]
    return "?"        