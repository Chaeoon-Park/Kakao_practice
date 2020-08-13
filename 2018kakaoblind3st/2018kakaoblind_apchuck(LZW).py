def solution(msg):
    answer = []
    dic = dict();
    alpha = 'A'
    alphanum = ord(alpha)
    newnum = 27
    for i in range (1,27) :
        im = {alpha : i}
        dic.update(im)
        alphanum = alphanum +1 
        alpha = chr(alphanum)


    i=-1
    while i<len(msg) :
        k = 1 
        i= i+1
        while True :
            nowmunza = msg[i:i+k]
            if dic.get(nowmunza)!=None :
                #마지막 문자에서 처리르 위함.
                if i+k == len(msg) :
                    answer.append(dic.get(nowmunza))
                    im = {msg[i:i+k] : newnum}
                    newnum = newnum+1
                    dic.update(im)
                    i = len(msg)
                    break
                else :
                    k= k+1
            else : 
                #없으면 단순히 넣어주면 됩니다
                answer.append(dic.get(msg[i:i+k-1]))
                im = {msg[i:i+k] : newnum}
                newnum = newnum+1
                i = i+k-2 # + -값을 알자네? 
                dic.update(im)
                break

        
    return answer

a=1
solution("TOBEORNOTTOBEORTOBEORNOT")