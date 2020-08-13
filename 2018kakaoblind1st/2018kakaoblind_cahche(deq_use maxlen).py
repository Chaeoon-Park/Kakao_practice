
#매우 중요함. 특히 콜랙션. ++ LRU 알고리즘은 새로운 캐시 들어오면 기존 캐시 지우고 새로 넣어야함

import collections as col
def solution(cacheSize, cities):
    answer = 0
    deq = col.deque(maxlen = cacheSize) #맥스랜이 정해지면 자동으로 앞에놈을 죽여버림

    for nowchache in cities :
        nowchache = nowchache.upper()
        flag =0
        for memorys in deq :
            if memorys == nowchache :
                flag =1
                break 
        if flag ==1 :
            deq.remove(nowchache)
            answer = answer +1
        else :
            answer = answer +5
        
        deq.append(nowchache)



    return answer

solution(3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"])