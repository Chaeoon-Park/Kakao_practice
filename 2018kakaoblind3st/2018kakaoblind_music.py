def solution(m, musicinfos):
    answer = ''
    anstime = 0

    m=m.replace("C#","H")
    m=m.replace("D#","I")
    m=m.replace("F#","J")
    m=m.replace("G#","K")
    m=m.replace("A#","L")

    for nowline in musicinfos :
        nowline = nowline.split(',')
        starttime = nowline[0].split(':')
        endtime = nowline[1].split(':')
        duringtime = int(endtime[0])*60 + int(endtime[1]) - int(starttime[0])*60 - int(starttime[1])
        nowline[3] = nowline[3].replace("C#","H")
        nowline[3] = nowline[3].replace("D#","I")
        nowline[3] = nowline[3].replace("F#","J")
        nowline[3] = nowline[3].replace("G#","K")
        nowline[3] = nowline[3].replace("A#","L")


        lenofmusic = len(nowline[3])
        mok = duringtime // lenofmusic #몫은 //
        namuzi = duringtime % lenofmusic #나머지는 %
        ans = ''
        for i in range (0,mok) :
            ans = ans + nowline[3]
        ans = ans + nowline[3][0:namuzi]
        flag = ans.find(m)
        if flag != -1 and anstime < duringtime :
            anstime = duringtime
            answer = nowline[2]
    if answer=='' :
            answer="(None)"
    return answer

solution("ABC", ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"])