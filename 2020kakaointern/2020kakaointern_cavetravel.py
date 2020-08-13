import collections as col
def solution(n, path, order):
    answer = True
    deq = col.deque()
    dic_child = dict()
    dic_need = dict()
    dic_cango = dict()
    need_visit = [False for i in range(0,n)]
    visit = [False for i in range(0,n)]

    
    for i in range(0,n) :
        dic_child.update({i : []})
        dic_need.update({i : 0 })
    for p in path :
        dic_child.get(p[0]).append(p[1])
        dic_child.get(p[1]).append(p[0])
    for o in order :
        dic_need.update({o[1] : o[0] })
        if o[1] == 0 :
            return False
        dic_cango.update({o[0] : o[1] })

    deq.append(0)
    #이게 사실상 레이지 거시기인가?
    while len(deq) != 0 :
        now = deq.popleft()
        visit[now]=True
        cango = dic_cango.get(now)
        child_list = dic_child.get(now)
        if cango != None and need_visit[cango] == True :
            deq.append(cango)
            need_visit[cango] = False
        for child in child_list :
            need = dic_need.get(child)
            if visit[need] == False :
                need_visit[child] = True
            elif visit[child]==False :
                deq.append(child)

    for i in range(n) :
        if visit[i] == False :
            return False
    return answer

solution(	2, [[1, 0]],[[1, 0]])