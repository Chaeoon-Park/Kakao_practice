def solution(N, stages):
    answer = []
    allstage =[[i,0,0,0] for i in range(N+2)]
    for stage in stages :
        for i in range(1,stage+1) :
            allstage[i][3] = allstage[i][3] +1
        allstage[stage][2] = allstage[stage][2]+1
    for i in range(0,N+2) :
        if allstage[i][3] == 0 :
            allstage[i][1] = 0
        else :
             allstage[i][1]= allstage[i][2] / allstage[i][3]
    allstage.sort(key = lambda x : (x[1], -x[0])) #- 붙이면 역순정렬
    for  i in range(N+1,-1,-1) :
        if allstage[i][0] != N+1 and  allstage[i][0] != 0 :
             answer.append(allstage[i][0])
    return answer

solution(	5, [2, 1, 2, 6, 2, 4, 3, 3])