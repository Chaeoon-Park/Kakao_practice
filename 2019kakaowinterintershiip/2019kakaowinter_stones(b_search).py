import copy
def solution(stones, k):
    answer = 0
    sortstone = copy.deepcopy(stones);
    sortstone.append(0)
    sortstone.sort()
    sortstone = list(set(sortstone))
    sortstone.append(sortstone[len(sortstone)-1]+1)
    min_p = min(sortstone)
    max_p = max(sortstone)
    mid_p = (min_p + max_p)//2
    while min_p <=max_p :
        middle = (min_p + max_p)//2
        cnt = 0 
        flag = True
        for stone in stones :
            if stone < middle :
                cnt = cnt+1    
                if cnt == k :
                    flag = False
                    break
            else :
                cnt = 0
        if flag==True :
            if middle >answer :
                answer = middle
            min_p = middle+1
              
        else :
            max_p = middle-1

    print(answer)
    return answer

#깝치지 말고 평범하게 이분탐색 하세요.. 충분히 n log n 이라 가능하네 지금보니까 가능하면 좀 안전하게 합시다.

solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3)