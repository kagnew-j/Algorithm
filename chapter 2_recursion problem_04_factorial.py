#chapter 2_recursion
#problem_04_factorial

# for문 팩토리얼
def fact_for(n):
    """
    for문 활용한 팩토리얼 값 반환 함수
    입력 : 자연수 값 n
    출력 : 1부터 n까지 연속한 숫자 곱한 값
    """
    f = 1                  # 곱셈 결과값 초기화 : 1
    for i in range(1,n+1): # 1부터 n까지 반복
        f *= i             # 결과값에 곱셈 연산
    return f
    
# recursion 팩토리얼
def fact_recur(n):
    """
    재귀 활용한 팩토리얼 값 반환 함수
    입력 : 자연수 값 n
    출력 : 1부터 n까지 연속한 숫자 곱한 값
    """
    if n in (1,2):               # 값이 1이나 2일 경우 
        return n                 # 바로 해당 값 반환
    else:                        # 그외의 경우
        return n*fact_recur(n-1) # n-1 함수값에 n을 곱하여 반환
        
# exercise 4-1
# recursion n_sum
def sum_recur(n):
    """
    재귀 활용한 자연수 n까지 연속합 반환 함수 
    입력 : 자연수 값 n
    출력 : 1부터 n까지 연속한 숫자 곱한 값
    """
    if n == 0:                   # 값이 1이나 2일 경우 
        return 0                 # 바로 해당 값 반환
    else:                        # 그외의 경우
        return n+sum_recur(n-1)  # n-1 함수값에 n을 더하여 반환

# exercise 4-2
# recursion find_max
## 스스로 짜지 않음.
def find_max_recur(a, n):
    """
    재귀 활용한 리스트에서 최댓값 반환 함수 
    입력 : 숫자열 list
    출력 : 최댓값
    """
    if n == 1:
        return a[0]
    max_n_1 = find_max_recur(a, n-1)
    if max_n_1 > a[n-1]:
        return max_n_1
    else:
        return a[n-1]