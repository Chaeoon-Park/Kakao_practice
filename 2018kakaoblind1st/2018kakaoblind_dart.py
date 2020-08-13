def solution(dartResult):
    answer = 0
    numbers = list();
    
    for i in range(0,len(dartResult)) :
        if dartResult[i] == 'S' :
            if i>=2 and dartResult[i-2]=='1' :
                snumber = dartResult[i-2:i]
            else :
                snumber = dartResult[i-1]
            numbers.append(int(snumber))

        elif dartResult[i] == 'D' :
            if i>=2 and dartResult[i-2]=='1' :
                snumber = dartResult[i-2:i]
            else :
                snumber = dartResult[i-1]
            numbers.append(int(snumber)**2)

        
        elif dartResult[i] == 'T' :
            if i>=2 and dartResult[i-2]=='1' :
                snumber = dartResult[i-2:i]
            else :
                snumber = dartResult[i-1]
            numbers.append(int(snumber)**3)        
        elif dartResult[i] == '*' :
            if(len(numbers)>1) :
                numbers[len(numbers)-1] = numbers[len(numbers)-1]*2
                numbers[len(numbers)-2] = numbers[len(numbers)-2]*2
            else :
                numbers[len(numbers)-1] = numbers[len(numbers)-1]*2
        elif dartResult[i] == '#' :
                numbers[len(numbers)-1] = numbers[len(numbers)-1]* (-1)

    for i in numbers :
        answer = answer + i

    return answer

solution("10S")