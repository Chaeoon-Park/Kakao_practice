from itertools import combinations
def checkexist(findlist, sets) :
    newlist = []
    for i in range(1, len(sets)) :
        newlist.append(list(combinations(sets, i)))
    for hlist in newlist :
        for nlist in hlist :
            if findlist.count(nlist) != 0 :
                return True
    return False

def checkkey(relation, sets) :
    imdic = []
    for real in relation :
        imkey = []
        for se in sets :
            imkey.append(real[se])
        if imdic.count(imkey) == 0 :
            imdic.append(imkey)
        else :
            return False
    return True

def solution(relation):
    answer = 0
    numtuple = len(relation[0])
    items = [ i for i in range(numtuple)]
    setlists = []
    findlist = []

    for i in range(1,numtuple+1) :
        setlists.append( list(combinations(items, i))   )

    for setlist in setlists :
        for sets in setlist :
            if checkexist(findlist, sets) == False :
                 if checkkey(relation,sets) == True :
                    findlist.append(sets) 
                    answer = answer+1
    return answer


solution([["100", "ryan", "music", "2"], ["200", "apeach", "math", "2"], ["300", "tube", "computer", "3"], ["400", "con", "computer", "4"], ["500", "muzi", "music", "3"], ["600", "apeach", "music", "2"]])