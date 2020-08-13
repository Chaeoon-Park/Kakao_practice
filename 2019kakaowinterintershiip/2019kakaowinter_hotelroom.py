
def solution(k, room_number):
    answer = []
    dic = dict()
    for room in room_number :
        if dic.get(room) == None :
            nextnum = room+1
            paths = [room]
            while dic.get(nextnum) != None :
                paths.append(nextnum)
                nextnum = dic.get(nextnum)
            for path in paths :
                dic.update({path : nextnum})
            answer.append(room)
        else :
            
            nownum = dic.get(room)
            paths = [room , nownum]
            while dic.get(nownum) != None :
                nownum = dic.get(nownum)
                paths.append(nownum)
            nextnum = nownum+1
            while dic.get(nextnum) != None :
                paths.append(nextnum)
                nextnum = dic.get(nextnum)
            for path in paths :
                dic.update({path : nextnum})
            answer.append(nownum)
    return answer

solution(	10, [1, 3, 4, 1, 3, 1])