def solution(str1, str2):
    answer = 0
    alphalist1 = [[0 for col in range(26)] for row in range(26)]
    alphalist2 =  [[0 for col in range(26)] for row in range(26)]
    
    small_a = ord('a')
    big_a = ord('A')
    realstr1 = list()
    realstr2 = list()
    for i in str1 :
        if (ord(i)>=small_a and ord(i)<=small_a+25) :
                realstr1.append(ord(i) - small_a)
        elif (ord(i)>=big_a and ord(i)<=big_a+25) :
                realstr1.append(ord(i) - big_a)
        else :
            realstr1.append(-1)
    for i in str2 :
        if (ord(i)>=small_a and ord(i)<=small_a+25) :
                realstr2.append(ord(i) - small_a)
        elif (ord(i)>=big_a and ord(i)<=big_a+25) :
                realstr2.append(ord(i) - big_a)
        else :
            realstr2.append(-1)

    for i in range(0,len(realstr1)-1) :
        if realstr1[i] != -1 and realstr1[i+1] != -1 :
              alphalist1[realstr1[i]][realstr1[i+1]] = alphalist1[realstr1[i]][realstr1[i+1]] + 1

    for i in range(0,len(realstr2)-1) :
        if realstr2[i] != -1 and realstr2[i+1] != -1 :
             alphalist2[realstr2[i]][realstr2[i+1]] = alphalist2[realstr2[i]][realstr2[i+1]] + 1


    g1 =0
    g2 =0
    for i in range(0,26) :
        for j in range(0,26) :
            g1 = g1 + min(alphalist1[i][j],alphalist2[i][j])
            g2 = g2 + max(alphalist1[i][j],alphalist2[i][j])

    if g2 !=0 :
       answer = int(float(float(g1)/float(g2))*65536)
    if g2==0 :
        answer = 65536
    print(answer)
    
    return answer

solution("aa1+aa2","AAAA12")