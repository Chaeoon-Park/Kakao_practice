
#이문제도 딕셔너리보다는 trie로 하는게 더 좋았을듯

import collections as col
import copy
def solution(words):
    answer = 0
    deq = col.deque()
    dic = dict();
    
    for word in words :
        if dic.get(word[0]) == None :
            im = {word[0] : [word]}
            dic.update(im)
            deq.append(word[0])
        else :
            ilist = dic.get(word[0])
            ilist.append(word)
            dic.update(im)
    
    while len(deq)!=0 :
        now = deq.popleft() #현재 탐색할 문자
        lennow = len(now)
        ilist = copy.deepcopy(dic.get(now))
        if len(ilist)== 1:
            answer = answer + lennow
        else :
            for nowword in ilist :
                if len(nowword) == lennow :
                     answer = answer + lennow
                else :
                    if dic.get(nowword[0:lennow+1]) == None :
                         im = {nowword[0:lennow+1] : [nowword]}
                         dic.update(im)
                         deq.append(nowword[0:lennow+1])
                    else :
                        (dic.get(nowword[0:lennow+1])).append(nowword)
        del dic[now]


    return answer


solution(["word", "war", "warrior", "world"])