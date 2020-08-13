from itertools import permutations
#조합은 컴비네이션으로 구할 수 있다.
import collections as col
import re
import copy
def solution(expression):
    answer = 0

    num_expression  = re.findall('\d+', expression) #+붙여야 숫자 전체로 인식해줌 안붙이면 56 이 5 6 이런식으로 따로
    for i in range(len(num_expression)) :
        num_expression[i] = int(num_expression[i])
    operand_expression = re.findall('[^0-9]', expression) # [] 붙이고 안에다가 ^가 아닌으로 가져 올 수 있음
    item = ['*','+','-']
    operands = list(permutations(item, 3))

    for operand in operands :
        deq = col.deque()
        for i in range(len(operand_expression)) :
            deq.append(num_expression[i])
            deq.append(operand_expression[i])
        deq.append(num_expression[len(num_expression)-1])

        for i in range(3) :
            nownum = -1
            newdeq = col.deque()
            while len(deq) !=0 :
                now = deq.popleft()
                
                if (type(now) == int) and nownum == -1 :
                    nownum = now
                elif now == operand[i] and now =='*' :
                    nextgap = deq.popleft()
                    nownum = nownum*nextgap
                elif now == operand[i] and now =='+' :
                    nextgap = deq.popleft()
                    nownum = nownum+nextgap
                elif now == operand[i] and now =='-' :
                    nextgap = deq.popleft()
                    nownum = nownum-nextgap
                elif type(now) != int :
                    newdeq.append(nownum)
                    newdeq.append(now)
                    nownum = -1
            newdeq.append(nownum)
            deq = copy.deepcopy(newdeq)

        gap = deq.popleft()    
        if abs(gap) > answer :
            answer = abs(gap)
    return answer

solution("100-200*300-500+20")