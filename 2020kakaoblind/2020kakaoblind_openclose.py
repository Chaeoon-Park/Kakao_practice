
import copy

def check(checklist) :
    cnt =0
    for i in checklist :
        if i=='(' :
            cnt = cnt+1
        elif i==')' :
            cnt = cnt-1
        if cnt<0 :
            return False

    return True

def divider(plist) :
    ocnt = 0
    ecnt = 0
    flag = 0
    for i in range(0,len(plist)) :
        if plist[i] == '(' :
            ocnt= ocnt +1
        elif plist[i] == ')' :
            ecnt = ecnt+1
        if ocnt == ecnt :
            flag = i
            break
    return plist[0:flag+1],plist[flag+1:len(plist)]


def dfs(copyp) :
    if copyp=='' :
        return ""

    u,v = divider(copyp)
    
    if check(u) == True :
        return u + dfs(v)
    else :
        imsi ="("
        imsi = imsi + dfs(v)
        imsi = imsi +")"
        u = u[1:len(u)-1]
        newu=""
        for x in u :
            if x=='(' :
                newu = newu+")"
            else :
                newu = newu+"("
        imsi = imsi + newu
        return imsi
def solution(p):
    answer = ''
    answer = dfs(p)
    print(answer)
    return answer

solution(")(")