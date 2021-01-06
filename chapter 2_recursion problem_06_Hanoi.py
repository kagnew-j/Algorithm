#chapter 2_recursion
#problem_06_Hanoi

# Hanoi
def hanoi(n, start, aux, end):
    """
    재귀 활용한 하노이의 탑 순서 출력 함수
    입력 n : 옮기려는 원반의 개수
         start : 출발점 기둥
         aux   : 보조 기둥
         end   : 목표 기둥
    """
    if n == 1: # 원반 1개인 경우 바로 옮기는 예외 처리
        print(start, "->", end)
        return
    # 시작에 있는 원반 n-1 개를 보조로 이동
    hanoi(n-1, start, end, aux)
    # 마지막 원반을 최종으로 이동
    print(start, "->", end)
    # 보조에 있는 원반 n-1 개를 최종으로 이동
    hanoi(n01, aux, start, end)
    
# exercise 6-1
# 모든 챕터 이후 재반복