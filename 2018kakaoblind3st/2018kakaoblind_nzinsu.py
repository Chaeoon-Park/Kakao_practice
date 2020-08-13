
def change(n,number) :
    imsi = ""
    Alpha = ['A','B','C','D','E','F']
    if number == 0 :
        return "0" 
    while number>0 :
        inum = number%n
        intoimsi =""
        if inum>=10 :
            intoimsi = Alpha[inum-10]
        else :
            intoimsi = str(inum)
        imsi = imsi + intoimsi
        number = number//n
    
    #문자열 뒤집기
    imsi = imsi[::-1]
    return imsi



def solution(n, t, m, p):
    answer = ''
    maxnum = t*m
    nums = ""
    
    for i in range(0,maxnum+1) :
        if len(nums) > maxnum :
            break
        else :
            nums = nums + change(n,i)
    
    for i in range(0,t) :
        answer = answer + nums[i*m + p -1]
    return answer

solution(16, 16, 2, 1)