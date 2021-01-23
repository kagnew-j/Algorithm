#chapter 3_search and sort
#problem_10_quick_sort

# 분할 정복(divide and conquer)
# 퀵 정렬 for easy explanation
def quick_sort_easy(a):
    """
    입력 : 리스트 a
    출력 : 없음, 정렬된 리스트 a
    """
    n = len(a)
    # 종료 조건
    if n <= 1:
        reutrn a 
    # 피벗 및 그룹 분할
    pivot = a[-1] # 편의상 마지막 원소를 기준 값으로 지정
    g1 = []
    g2 = []
    # 기준 값 정하고 기준에 맞춰 그룹 분할
    for i in range(n-1):
        if a[i] < pivot:
            g1.append(a[i])
        else:
            g2.append(a[i])
    return quick_sort_easy(g1)+[pivot]+quick_sort_easy(g2)

# Generalized Quick Sort
def quick_sort_sub(a, start, end):
    """
    입력 : 리스트 a, 시작범위 start, 종료범위 end
    출력 : 없음, 정렬된 리스트 a
    """
    # 종료 조건
    if end-start<= 0:
        return
    # 피벗 및 그룹 분할 후 정렬
    pivot = a[end]
    i = start
    for j in range(start,end):
        if a[j] <= pivot:
            a[i], a[j] = a[j], a[i]
            i += 1
    a[i], a[end] = a[end], a[i]
    # 재귀 호출 정렬
    quick_sort_sub(a,start,i-1)
    quick_sort_sub(a,i+1,end)


def quick_sort_gen(a):
    quick_sort_sub(a,0,len(a)-1)