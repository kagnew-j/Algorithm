#chapter 5_applied algorithm
#problem_16_graph mazerunner

# maze modeling
maze = {
    'a':['e'],
    'b':['c','f'], 
    'c':['b','d'], 
    'd':['c'], 
    'e':['a','i'],
    'f':['b','g','j'],
    'g':['f','h'],
    'h':['g','l'],
    'i':['e','m'],
    'j':['f','k','n'],
    'k':['j','o'],
    'l':['h','p'],
    'm':['i','n'],
    'n':['m','j'],
    'o':['k'],
    'p':['l']
} 

# maze runner
def solve_maze(g, start, end):
    """
    메이즈러너
    입력 : 미로 그래프 g, 출발점 start, 도착점 end
    출력 : 출발점에서 도착점까지의 이동 경로 문자열, 없을 경우 물음표 ?
    """
    qu = []
    done = set()

    qu.append(start)
    done.add(start)

    while qu:
        p = qu.pop(0)
        v = p[-1]
        if v == end:
            return p
        for x in g[v]:
            if x not in done:
                qu.append(p+x)
                done.add(x)
    # 탐색이 끝나도 도착점이 나오지 않는다면 미로이므로 ? 반환
    return "?"

print(solve_maze(maze,'a','p'))
# aeimnjfghlp