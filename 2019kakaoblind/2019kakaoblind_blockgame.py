

import copy

def solution(board):
    answer = 0
    dic = dict()

    rotater =[
        [[0,1],[0,2],[1,2]],
        [[1,0],[2,0],[0,1]],
        [[1,0],[1,1],[1,2]],
        [[0,1],[-1,1],[-2,1]],

        [[1,0],[0,1],[0,2]],
        [[1,0],[2,0],[2,1]],
        [[0,1],[0,2],[-1,2]],
        [[0,1],[1,1],[2,1]],

        [[0,1],[-1,1],[0,2]],
        [[1,0],[2,0],[1,1]],
        [[0,1],[1,1],[0,2]],
        [[-1,1],[0,1],[1,1]]
    ]

    filler = [
        [[1,0],[1,1]],
        [[1,1],[2,1]],
        [[0,1],[0,2]],
        [[-1,0],[-2,0]],

        [[1,1],[1,2]],
        [[0,1],[1,1]],
        [[-1,0],[-1,1]],
        [[1,0],[2,0]],

        [[-1,0],[-1,2]],
        [[0,1],[2,1]],
        [[1,0],[1,2]],
        [[-1,0],[1,0]]
    ]
    
    for i in range(len(board)) :
        for j in range(len(board)) :
            if board[i][j] != 0 :
                if dic.get(board[i][j])== None :
                    dic.update({board[i][j] : [[i,j]]})
                else :
                    dic.get(board[i][j]).append([i,j])

    flag = 1
    while flag != 0 :
        nowboard = copy.deepcopy(board)
        tops = [len(board) for i in range(len(board)) ]
        for i in range(len(board)) :
            for j in range(len(board)) :
                if board[j][i] != 0 :
                    tops[i] = j
                    break


        diclist = list(dic.keys())
        flag = 0
        for nownum in diclist :
            nums = dic.get(nownum)
            nums.sort(key = lambda x : (x[1], x[0]))
            nowx = nums[0][0]
            nowy = nums[0][1]
            findshape = -1
            
            for r in range(12) :
                nowflag =0
                for roatate in rotater[r] :
                    if [roatate[0]+nowx, roatate[1]+nowy] not in nums :
                        nowflag=1
                        break
                if nowflag==0 :
                    findshape = r
                    break
            
            if nowboard[nowx + filler[findshape][0][0]][nowy + filler[findshape][0][1]] == 0 and nowboard[nowx + filler[findshape][1][0]][nowy + filler[findshape][1][1]] == 0 and nowx + filler[findshape][0][0] < tops[nowy + filler[findshape][0][1]] and nowx + filler[findshape][1][0] < tops[nowy + filler[findshape][1][1]] :
                flag = 1
                answer = answer+1
                for dele in nums :
                    board[dele[0]][dele[1]] = 0
                del dic[nownum]
 
    return answer


solution([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 4, 0, 0, 0], [0, 0, 0, 0, 0, 4, 4, 0, 0, 0], [0, 0, 0, 0, 3, 0, 4, 0, 0, 0], [0, 0, 0, 2, 3, 0, 0, 0, 5, 5], [1, 2, 2, 2, 3, 3, 0, 0, 0, 5], [1, 1, 1, 0, 0, 0, 0, 0, 0, 5]])