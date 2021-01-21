#chapter 3_search and sort
#problem_10_merge_sort

# 분할 정복(divide and conquer)
# 병합 정렬 for easy explanation
def merge_sort_easy(a):
    """
    입력 : 리스트 a
    출력 : 없음. 정렬된 리스트 a
    """
    n = len(a)
    # 종료 조건
    if n <= 1:
        reutrn a 
    # 그룹 나누어 병합 정렬 호출
    mid = n // 2
    g1 = merge_sort_easy(a[:mid])
    g2 = merge_sort_easy(a[mid:])
    # 두 그룹 병합
    result = []
    while g1 and g2:
        if g1[0] < g2[0]:
            result.append(g1.pop(0))
        else:
            result.append(g2.pop(0))
    while g1:
        result.append(g1.pop(0))
    while g2:
        result.append(g2.pop(0))
    return result

# Generalized Merge Sort
def merge_sort_gen(a):
    n = len(a)
    # 종료 조건
    if n <= 1:
        return
    # 그룹 분할 하여 병합 정렬 호출
    mid = n // 2
    g1 = merge_sort_gen(a[:mid])
    g2 = merge_sort_gen(a[mid:])
    # 두 그룹 병합
    i1, i2, ia = 0, 0, 0
    while i1 < len(g1) and i2 < len(g2):
        if g1[i1] < g2[i2]:
            a[ia] = g1[i1]
            i1 += 1
            ia += 1
        else:
            a[ia] = g2[i2]
            i2 += 1
            ia += 1
    # 남아있는 자료 결과에 추가
    while i1 < len(g1):
        a[ia] = g1[i1]
        i1 += 1
        ia += 1
    while i2 < len(g2):
        a[ia] = g2[i2]
        i2 += 1
        ia += 1
        
# exercise 9-1
# reverse merge sort  
def merge_sort_rev(a):
    n = len(a)
    # 종료 조건
    if n <= 1:
        return
    # 그룹 분할 하여 병합 정렬 호출
    mid = n // 2
    g1 = merge_sort_rev(a[:mid])
    g2 = merge_sort_rev(a[mid:])
    # 두 그룹 병합
    i1, i2, ia = 0, 0, 0
    while i1 < len(g1) and i2 < len(g2):
        if g1[i1] > g2[i2]:
            a[ia] = g1[i1]
            i1 += 1
            ia += 1
        else:
            a[ia] = g2[i2]
            i2 += 1
            ia += 1
    # 남아있는 자료 결과에 추가
    while i1 < len(g1):
        a[ia] = g1[i1]
        i1 += 1
        ia += 1
    while i2 < len(g2):
        a[ia] = g2[i2]
        i2 += 1
        ia += 1