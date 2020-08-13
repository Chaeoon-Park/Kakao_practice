
def solution(lines) :
    answer = 0
    startdays =list()
    enddays=list()
    gugans = list()
    dic = dict()
    cnt = 0
    for pipeline in lines :
        pipeline=pipeline.split()
        date = pipeline[0].split('-')
        time = pipeline[1].split(':')
        during = pipeline[2][0:-1] 
        endtime = float(time[0])*3600 + float(time[1])*60 + float(time[2])
        startdate = float(endtime) - float(during) +0.001
        startdays.append(startdate)
        enddays.append(endtime)
        gugans.append(startdate)
        gugans.append(endtime+0.9999)
        dic.update({startdate : 0})
        dic.update({endtime+0.9999 : 1})
        cnt = cnt+1

    #실행에 포함될수 있는 구간을 먼저 만들어 버리는 방법.
    
    worktime = 0
    gugans.sort()
    for gugan in gugans :
        if dic.get(gugan) == 0 :
            worktime = worktime +1
        else :
            worktime = worktime -1
        if worktime > answer :
            answer = worktime

    return answer


def solution1(lines):
    answer = 0
    startdays =list()
    enddays=list()
    for pipeline in lines :
        pipeline=pipeline.split()
        date = pipeline[0].split('-')
        time = pipeline[1].split(':')
        during = pipeline[2][0:-1] 
        endtime = float(time[0])*3600 + float(time[1])*60 + float(time[2])
        startdate = float(endtime) - float(during)
        startdays.append(startdate)
        enddays.append(endtime)

    n = len(startdays)
    for i in range(0,n) :
        t1 = 0
        t2 = 0
        for j in range(0,n) :
            if startdays[i]<enddays[j] and startdays[i]+1 >startdays[j] :
                t1 =t1 +1
            if enddays[i]-0.001 <  enddays[j] and  enddays[i]+0.999 > startdays[j] :
                t2 =t2 +1
        if(t1>answer) :
            answer = t1
        if(t2>answer) :
            answer = t2
    print(answer)
    return answer
    

solution( 			["2016-09-15 23:59:59.999 0.001s"])

