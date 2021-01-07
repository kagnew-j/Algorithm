#chapter 3_search and sort
#problem_12_binary search

# binary search
def bsearch(a, x):
    """
    이분 탐색 활용한 타겟 위치 출력 함수
    입력 : 리스트 a, 타겟 x
    출력 : 값의 위치, else -1
    """
    start = 0
    end = len(a) - 1

    while start <= end:
        mid = (start + end)//2
        if x == a[mid]:
            return mid
        elif x > a[mid]:
            start = mid + 1
        else:
            end = mid - 1
    return -1    

d = [1,4,9,16,25,36,49,64,81]
print(bsearch(d,36))
print(bsearch(d,50))

# exercise 12-1
# recursion binary search
def bsearch_recur_sub(a,x,start,end):
    """
    재귀를 사용한 이분 탐색 활용한 타겟 위치 출력 함수 보조 모듈
    입력 : 리스트 a, 타겟 x
    출력 : 값의 위치, else -1
    """
    if start > end:
        return -1
    
    mid = (start + end) //2
    if x == a[mid]:
        return mid
    elif x > a[mid]:
        return bsearch_recur_sub(a,x,mid+1,end)
    else:
        return bsearch_recur_sub(a,x,start, mid-1)
    return -1

def bsearch_recur(a,x):
    """
    재귀를 사용한 이분 탐색 활용한 타겟 위치 출력 함수
    입력 : 리스트 a, 타겟 x
    출력 : 값의 위치, else -1
    """
    return bsearch_recur_sub(a,x,0,len(a)-1)

d = [1,4,9,16,25,36,49,64,81]
print(bsearch_recur(d,36))
print(bsearch_recur(d,50))