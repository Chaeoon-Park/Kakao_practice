#dfs로 다시할것 이문제는 틀렸다 확실히 permutation은 순서있는 조합

from itertools import permutations
    

def solution(n, weak, dist):
    answer = 99999999
     #모든 조합 생성 방법0
    items = [i for i in range(0,len(dist))]
    setlists = list(permutations(items, len(dist)))   
    #모든 조합 생성 방법
    wlen = len(weak)
    for i in range (0,wlen) :
        weak.append(weak[i]+n)
    
    for start_point in range (0,wlen) :
        for setlist in setlists :
            cnt = 0
            now_point = start_point
            now_dist_point = 0
            if setlist == (2,1,0,3) and start_point ==1 :
                start_point =1
            while now_dist_point < len(dist) :
                now_point_cnt = 1
                cnt = cnt + 1
                if cnt == wlen :
                    if now_dist_point + 1 < answer :
                        answer = now_dist_point + 1 
                    break
                while weak[now_point + now_point_cnt] - weak[now_point] <= dist[setlist[now_dist_point]] :
                    now_point_cnt = now_point_cnt+1
                    cnt = cnt + 1
                    if cnt == wlen :
                        break
                if cnt == wlen :
                    if now_dist_point + 1 < answer :
                        answer = now_dist_point + 1 
                    break
                now_dist_point = now_dist_point+1
                now_point = now_point + now_point_cnt
    if answer = 99999999 :
        answer = -1

    return answer

solution(	12, [1, 5, 6, 10], [1, 2, 3, 4])