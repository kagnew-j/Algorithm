#chapter 3_search and sort
#problem_09_insertion_sort

# 삽입 정렬 for easy explanation
def find_ins_idx(r,v):
    """
    for문 활용한 삽입 위치 반환 함수
    입력 : 리스트 r, 삽입될 숫자값 v
    출력 : 삽입해야할 index
    """
    for i in range(len(r)): # 이미 정렬된 리스트를 앞에서부터 확인
        if v < r[i]:        # v값보다 i번 위치 값이 크면
            return i        # i 위치 반환, v값이 현 i 위치 앞에 놓이려면 i 번째 삽입해야함.
    return len(r)           # 적절한 위치 반환 없을시 제일 큰 수 이므로 맨 뒤에 삽입

def ins_sort(a):
    """
    for문 활용한 삽입 리스트 정렬
    입력 : 리스트 a
    출력 : 정렬된 리스트 a
    """
    result = []                              # 정렬된 값을 저장할 새 리스트
    while a:                                 # 기존 리스트에 값이 남아 있는 동안 반복
        value = a.pop(0)                     # 기존 리스트에서 제일 첫번째 값 꺼냄
        ins_idx = find_ins_idx(result,value) # 꺼낸 값이 들어갈 위치 찾기
        result.insert(ins_idx, value)        # 찾은 위치에 값 삽입
    return result                            # 결과 리스트 반환

# Generalized Insertion Sort
def ins_sort_gen(a):
    """
    for문 활용한 삽입 리스트 정렬
    입력 : 리스트 a
    출력 : 정렬된 리스트 a
    """
    n = len(a)
    for i in range(1,n):             # 1부터 n-1까지
        key = a[i]                   # key에 i번 위치 값 저장
        j = i-1                      # j에 바로 i번 왼쪽 위치 값 저장
        while j >= 0 and a[j] > key: # j가 0보다 크거나 같고, 값이 key 보다 큰 경우
            a[j+1] = a[j]            # 삽입할 공간이 생기도록 값을 오른쪽으로 한 칸 이동
            j -= 1
        a[j+1] = key                 # 찾은 삽입 위치에 key 값 삽입

# exercise 9-1
# Done by hands

# exercise 9-2
# reverse insertion sort    
def ins_sort_rev(a):
    """
    for문 활용한 삽입 리스트 정렬
    입력 : 리스트 a
    출력 : 정렬된 리스트 a
    """
    n = len(a)
    for i in range(1,n):             # 1부터 n-1까지
        key = a[i]                   # key에 i번 위치 값 저장
        j = i-1                      # j에 바로 i번 왼쪽 위치 값 저장
        while j >= 0 and a[j] < key: # j가 0보다 크거나 같고, 값이 key 보다 작은 경우
            a[j+1] = a[j]            # 삽입할 공간이 생기도록 값을 오른쪽으로 한 칸 이동
            j -= 1
        a[j+1] = key                 # 찾은 삽입 위치에 key 값 삽입  