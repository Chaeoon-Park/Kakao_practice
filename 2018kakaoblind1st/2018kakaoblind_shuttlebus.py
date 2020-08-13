def solution(n, t, m, timetable):
    answer = ''
    dic=dict()
    timer = 9*60
    for i in range (0,n) :
        im ={timer : 0}
        dic.update(im)
        timer = timer + t
    
    
    diclist = list(dic.keys())

    timelist = list()
    for tut in timetable :
        tut = tut.split(':')
        timelist.append(int(tut[0])*60 + int(tut[1]))
    timelist.sort()
    

    lasttime = 0
    
    for num  in timelist :
        for bustime in diclist :
            if bustime>=num and dic.get(bustime)<m :
                dic[bustime] = dic.get(bustime) + 1
                lasttime = num
                break



    if dic.get(diclist[len(diclist)-1]) >=m : 
        getintime = lasttime-1
    else :
        getintime = diclist[len(diclist)-1]


    hour = int(getintime/60)
    minuate = getintime - hour*60

    if hour<10 :
        answer = answer +'0' + str(hour)
    else :
        answer = answer + str(hour)
    
    answer = answer + ':'

    if minuate<10 :
        answer = answer +'0' + str(minuate)
    else :
        answer = answer + str(minuate)

    return answer


solution(2, 10, 2, ["09:10", "09:09", "08:00"])