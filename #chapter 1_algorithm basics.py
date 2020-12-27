#chapter 1_algorithm basics
#problem_01_n_sum

#연속숫자 합 1
def sum_brute(n):
    """
    자연수 n까지 연속합 반환 함수 
    입력 : 자연수 값 n
    출력 : 연속합 값
    """
    s = 0                   # 합계 0으로 초기화
    for i in range(1,n+1):  # 1부터 n까지 반복
        s = s + i           # 합계에 더함
    return s

# 연속숫자 합 2
def sum_math(n):
    """
    자연수 n까지 연속합 반환 함수 
    입력 : 자연수 값 n
    출력 : 연속합 값
    """
    return n*(n+1)//2  # 수학 공식 사용하여 합계 계산

# exercise 1-1
# 연속 숫자의 제곱합 1
def square_sum_brute(n):
    """
    자연수 n까지 연속 제곱합 반환 함수 
    입력 : 자연수 값 n
    출력 : 연속합 값
    """
    s = 0                   # 합계 0으로 초기화
    for i in range(1,n+1):  # 1부터 n까지 반복
        s = s + i**2        # 합계에 더함
    return s

# exercise 1-2
# O(n)

# exercise 1-3
# 연속 숫자의 제곱합 1
def square_sum_math(n):
    """
    자연수 n까지 연속 제곱합 반환 함수 
    입력 : 자연수 값 n
    출력 : 연속합 값
    """
    return n*(n+1)*(2*n+1)//6  # 수학 공식 사용하여 합계 계산

##################################################################

#problem_02_find_max

# 최댓값 찾기
def find_max_brute(a):
    """
    최댓값 반환 함수
    입력 : 숫자가 들어 있는 list
    출력 : 최댓값
    """
    n = len(a)            # 입력 크기 n
    max_v = a[0]          # 리스트의 첫 번째 값 최댓값으로 지정
    for i in range(1,n):  # 1부터 n-1까지 반복
        if a[i] > max_v:  # 이번 값이 최댓값보다 크면
            max_v = a[i]  # 최댓값 교체
    return max_v

# 최댓값 위치 찾기
def find_max_idx(a):
    """
    최댓값 위치 반환 함수
    입력 : 숫자가 들어 있는 list
    출력 : 최댓값의 인덱스 값
    """
    n = len(a)                 # 입력 크기 n
    max_idx = 0                # 최댓값 위치 0으로 초기화
    for i in range(1,n):       # 1부터 n-1까지 반복
        if a[i] > a[max_idx]:  # 이번 값이 최댓값보다 크면
            max_idx = i        # 최댓값 위치 변경
    return max_idx

# exercise 2-1
# 최솟값 찾기
def find_min_brute(a):
    """
    최솟값 반환 함수
    입력 : 숫자가 들어 있는 list
    출력 : 최솟값
    """
    n = len(a)            # 입력 크기 n
    min_v = a[0]          # 리스트의 첫 번째 값 최솟값으로 지정
    for i in range(1,n):  # 1부터 n-1까지 반복
        if a[i] < min_v:  # 이번 값이 최솟값보다 크면
            min_v = a[i]  # 최솟값 교체
    return min_v

##################################################################

#problem_03_same_name

# 동명이인 찾기
def samename(a):
    """
    같은 이름 찾는 함수
    입력 : 이름이 들어 있는 list
    출력 : 반복 되는 이름의 set
    """
    n = len(a)                    # 리스트 자료 개수를 n에 저장
    result = set()                # 결과 저장할 빈 집합 생성
    for i in range(n-1):          # 0 부터 n-2 반복
        for j in range(i+1,n):    # i+1 부터 n-1까지 반복
            if a[i] == a[j]:      # 이름이 같으면 집합에 추가
                result.add(a[i])
    return result

# exercise 3-1
# 조합 출력하기
def comb_people(a):
    """
    모든 2인 조합 반환 함수(입력 리스트 중복 없다 가정)
    입력 : 사람 이름들이 들어 있는 list
    출력 : 모든 조합 화면에 출력
    """
    n = len(a)                                # 입력 크기 n
    for i in range(n-1):                      # 0 부터 n-2 까지 반복
        for j in range(i+1,n):                # i+1 부터 n-1 까지 반복
            print(a[i], "-", a[j], sep = " ") # 가운데 공백을 두고 출력

# exercise 3-2
# A : O(1)
# B : O(n)
# C : O(n^2)
# D : O(n^4)