
#제일 심각히 못푼 문제 문제는 index 구분이였는데 왜 문제인지 아직도 잘 모르겠음 작은 실수에서 ㅈ되는것좀 조심하자

import copy
def solution(files):
    answer = []
    int_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    for nf in files :
        flag = 0
        eflag =0
        nowfile = copy.deepcopy(nf)
        nowfile = nowfile.lower()
        for i in range(0,len(nowfile)) :
            if nowfile[i] in int_list :
                    flag = i 
                    break
        
        for i in range(flag,flag+5) :
            if i==len(nowfile) :
                eflag = i -1
                break
            elif nowfile[i] not in int_list :
                eflag = i -1
                break
            else :
                eflag = i       
        if eflag==0 :
            eflag = len(nowfile)
        if eflag-flag >4 :
            eflag =flag + 4 
        
        #2
        answer.append([nowfile[:flag],int(nowfile[flag:eflag+1]),nowfile[eflag+1:],nf])
        answer.sort(key = lambda x : (x[0], x[1]))
        
    
    
    answer = [j[3] for j in answer]
    return answer






solution(	["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"])



