#속도 높일때는 딕셔너리가 필수야 효율성 문제에서는 딕셔너리 활용에 대해 꼭 생각해볼 것

import collections as col


def solution(gems):
    answer = []
    minlen = 99999999
    deq = col.deque()
    gem_list = list(set(gems))
    gem_dic = dict()
    for gem in gem_list :
        gem_dic.update({gem : 0})

    length = len(gem_list)
    tail = length
    head = 0
    gem_flag = -1
    no_gems = 0
    for i in range(head,tail) :
        deq.append(gems[i])
        if gem_dic.get(gems[i]) == 0 :
            no_gems = no_gems +1
        gem_dic.update({gems[i] : gem_dic.get(gems[i])+1})
    


    for i in range(length,len(gems)+1) :

        while  gem_dic.get(deq[0])> 1 :
            head = head+1
            gem_dic.update({deq[0] : gem_dic.get(deq[0])-1})
            im = deq.popleft() 
        
        
        if no_gems == length and minlen > len(deq) :
            minlen = len(deq)
            answer = [head+1,tail]

        if i != len(gems) :
            if gem_dic.get(gems[i]) == 0 :
                no_gems = no_gems+1

            deq.append(gems[i])
            gem_dic.update({gems[i] : gem_dic.get(gems[i])+1 })
            tail = tail + 1
            
    
    return answer

solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"])