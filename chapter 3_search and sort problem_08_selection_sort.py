#chapter 3_search and sort
#problem_08_selection_sort

# 선택 정렬 for easy explanation
def find_min_idx(a):
    """
    
    """
    n = len(a)
    min_idx = 0
    for i in range(1,n):
        if a[i] < a[min_idx]:
            min_idx = i
    return min_idx

def sel_sort_simple(a):
    """
    
    """    
    result = []
    while a:
        min_idx = find_min_idx(a)
        value = a.pop(min_idx)
        result.append(value)
    return result

# Generalized Selection Sort
def sel_sort_gen(a):
    """
    
    """
    n = len(a)
    for i in range(n-1):
        min_idx = i
        for j in range(i+1,n):
            if a[j] < a[min_idx]:
                min_idx = j
        a[i],a[min_idx] = a[min_idx], a[i]        

# exercise 8-1
# Done by hands

# exercise 8-2
# reverse selection sort
def sel_sort_rev(a):
    """
    
    """
    n = len(a)
    for i in range(n-1):
        max_idx = i
        for j in range(i+1,n):
            if a[j] > a[max_idx]:
                max_idx = j
        a[i],a[max_idx] = a[max_idx], a[i]      