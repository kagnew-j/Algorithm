#chapter 5_applied algorithm
#problem_17_fake coin 

# 무게 비교 함수
def weigh(a, b, c, d, fake = 29):
    """
    주어진 동전 n개 중에 가짜 동전(fake)를 찾는 알고리즘
    입력: 전체 동전 위치의 시작과 끝 (0,n-1)
        : a 에서 b까지 놓인 동전
        : c 에서 d까지 놓인 동전
    출력: 가짜 동전의 위치 번호
        : a에서 b까지 가짜 동전이 있으면(가벼우면): -1
        : c에서 d까지 가짜 동전이 있으면(가벼우면): 1
        : 가짜 동전이 없으면(양쪽 무게가 같으면): 0 
    """
    # fake = 29 # 가짜 동전의 위치 # 변수 처리
    if a <= fake and fake <= b:
        return -1
    if c<= fake and fake <= d:
        return 1
    return 0

# 무게 비교 함수를 사용하여 가짜 동전의 위치 찾기
def find_fakecoin(left, right):
    for i in range(left+1, right+1): # left+1 부터 right까지 반복
        result = weigh(left, left, i, i)
        # 가장 왼쪽 동전과 나머지 동전을 차례로 비교
        if result == -1:
            return left
        elif result == 1:
            return i
        # 두 동전의 무게가 같으면 다음 동전으로 이동
    # 모든 동전의 무게가 같음 : 가짜 동전 없는 예외 경우
    return -1

n = 1000 # 전체 동전 개수
print(find_fakecoin(0,n-1))