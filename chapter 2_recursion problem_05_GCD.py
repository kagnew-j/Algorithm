#chapter 2_recursion
#problem_05_GCD, Great Common Divider

# while문 GCD_brute
def gcd_brute(a,b):
    """
    while문 활용한 최대공약수 반환 함수
    입력 : 자연수 값 a, b
    출력 : a, b 최대공약수
    """
    i = min(a,b)                      # 최솟값을 시작 값으로 세팅
    while True:                       # return 전까지 반복
        if a % i == 0 and b % i == 0: # 값이 두 수를 나눌 수 있으면
            return i                  # 결과값 return
        i -= 1

# GCD_recur
def gcd_recur(a,b):
    """
    재귀 활용한 최대공약수 반환 함수
    입력 : 자연수 값 a, b
    출력 : a, b 최대공약수
    """
    if b == 0:
        return a
    return gcd_recur(b, a%b)

# exercise 5-1
# recursion fibonacci
def fibo_recur(n):
    """
    재귀 활용한 피보나치 수열값 반환 함수 
    입력 : 피보나치 수열값 위치
    출력 : 수열값
    """
    if n in (0,1):
        return n
    return fibo_recur(n-1)+fibo_recur(n-2)