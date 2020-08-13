def solution(s):
    answer = 0
    slen =len(s)
    minlen = slen
    for i in range(1,slen//2 +1) :
        mok = slen // i
        flag = 0
        cnt = 0
        allcnt = 0
        nowcnt=0
        for j in range(0,mok+1) :
            if allcnt== 49 :
                j=j
            if i*(j+2) <=slen : 
                if s[j*i:i*(j+1)] == s[i*(j+1) : i*(j+2)] :
                    allcnt = allcnt+1
                    nowcnt = nowcnt+1
                    if flag==0 :
                        flag=1
                        cnt= cnt+1
                    if i*(j+2) == slen :
                        nowcnt = nowcnt+1
                        if nowcnt >=10 and 100 > nowcnt  :
                             cnt = cnt+1
                        if nowcnt >=100 and 1000 > nowcnt  :
                             cnt = cnt+2
                        if nowcnt ==1000  :
                             cnt = cnt+3   
                        break

                else :
                    flag =0
                    nowcnt = nowcnt+1
                    if nowcnt >=10 and 100 > nowcnt  :
                        cnt = cnt+1
                    if nowcnt >=100 and 1000 > nowcnt  :
                        cnt = cnt+2
                    if nowcnt ==1000  :
                        cnt = cnt+3    
                    nowcnt = 0        
            else :
                    flag =0
                    nowcnt = nowcnt+1
                    if nowcnt >=10 and 100 > nowcnt  :
                        cnt = cnt+1
                    if nowcnt >=100 and 1000 > nowcnt  :
                        cnt = cnt+2
                    if nowcnt ==1000  :
                        cnt = cnt+3    
                    nowcnt = 0     
                    break         


        if minlen > slen - allcnt*i +cnt :
            minlen = slen - allcnt*i + cnt
    answer = minlen
    print(answer)
    return answer

solution("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaac")



