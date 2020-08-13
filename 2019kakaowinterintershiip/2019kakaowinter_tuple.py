import re

def solution(s):
    answer = []
    s = s[1:-1]
    parser = re.compile('{(.+?)}')
    ituples = parser.findall(s)
    tuples =[]
    for ituple in ituples :
        t=ituple.split(',')
        length = len(t)
        tuples.append([t , length])
    tuples.sort(key = lambda x : x[1])
    for i in range(len(tuples)) :
        for tup in tuples[i][0] :
            if int(tup) not in answer :
                answer.append(int(tup))
    #(.+?)
    answer = answer
    return answer

solution("{{20,111},{111}}")