def solution(numbers, hand):
    answer = ''

    numpad = [[3,1],
              [0,0],
              [0,1],
              [0,2],
              [1,0],
              [1,1],
              [1,2],
              [2,0],
              [2,1],
              [2,2]
                ]
    Lefthand = [3,0]
    Righthand = [3,2]

    for i in numbers :
        next_x = numpad[i][0]
        next_y = numpad[i][1]
        if next_y == 2 :
            Righthand = [next_x , next_y]
            answer=answer+'R'

        elif next_y == 0 :    
            Lefthand = [next_x , next_y]
            answer=answer+'L'
        
        else :
            D_r = abs(next_x - Righthand[0]) + abs(next_y - Righthand[1])
            D_l = abs(next_x - Lefthand[0]) + abs(next_y - Lefthand[1])
            if D_r<D_l or (D_r==D_l and hand=="right"):
                Righthand = [next_x , next_y]
                answer=answer+'R'

            elif D_r>D_l or (D_r==D_l and hand=="left"):
                Lefthand = [next_x , next_y]
                answer=answer+'L'


    return answer

solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5],"right")