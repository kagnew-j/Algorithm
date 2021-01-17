#chapter 4_data structure
#problem_15_graph 그래프

# 실험용 데이터
fr_info = {
    'Summer':['John','Justin','Mike'],
    'John':['Summer','Justin'],
    'Justin':['John','Summer','Mike','May'],
    'Mike':['Summer','Justin'],
    'May':['Justin','Kim'],
    'Kim':['May'],
    'Tom':['Jerry'],
    'Jerry':['Tom']
}
# 친구의 친구 찾기 every connected node with Queue
def print_all_friends(g, start):
    """
    친구 리스트에서 자신의 모든 친구를 찾는 알고리즘
    입력 : 친구 관계 그래프(딕셔너리) g, 모든 친구를 찾을 start
    출력 : 모든 친구의 이름
    """
    qu = [] # Memory 1 : person to process
    done = set() # Memory 2 : person done processing

    qu.append(start) # 자신을 큐에 넣고 시작
    done.add(start)  # 자신을 집합에도 추가

    while qu:
        p = qu.pop(0)
        print(p)
        for x in g[p]:
            if x not in done:
                qu.append(x)
                done.add(x)
# Test run
print_all_friends(fr_info,"Summer")
print()
print_all_friends(fr_info,"Jerry")

# 친밀도 계산 알고리즘 : 촌수
def print_all_friends_dist(g, start):
    """
    친구 리스트에서 자신의 모든 친구를 찾는 알고리즘
    입력 : 친구 관계 그래프(딕셔너리) g, 모든 친구를 찾을 start
    출력 : 모든 친구의 이름
    """
    qu = [] # Memory 1 : person to process
    done = set() # Memory 2 : person done processing

    qu.append((start,0)) # 자신을 큐에 넣고 시작
    done.add(start)  # 자신을 집합에도 추가

    while qu:
        (p, d) = qu.pop(0)
        print(p, d)
        for x in g[p]:
            if x not in done:
                qu.append((x, d+1))
                done.add(x)
# Test run
print_all_friends_dist(fr_info,"Summer")
print()
print_all_friends_dist(fr_info,"Jerry")

# exercise 15-1
# 실험용 데이터
nd_info = {
    1:[2, 3],
    2:[1, 4, 5],
    3:[1],
    4:[2],
    5:[2],
}

def bfs(g, start):
    """
    그래프 너비 우선 탐색
    입력 : 그래프(딕셔너리) g, 시작점 start
    출력 : 모든 연경된 노드 명
    """
    qu = [] # Memory 1 : node to process
    done = set() # Memory 2 : node done processing

    qu.append(start) # 자신을 큐에 넣고 시작
    done.add(start)  # 자신을 집합에도 추가

    while qu:
        p = qu.pop(0)
        print(p)
        for x in g[p]:
            if x not in done:
                qu.append(x)
                done.add(x)

# Test run
bfs(nd_info, 1)