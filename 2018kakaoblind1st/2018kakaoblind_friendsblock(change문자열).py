
import copy

def cntboard(new_board,countboard,x,y) :
    if countboard[x][y] == 0 :
        countboard[x][y]=1
        new_board[x] = new_board[x][:y]+'0' + new_board[x][y+1:]   #문자열 치환 방법 굉장히 중요 한번에 안되고 파싱해서 줘야함

        return 1    
    else :
        new_board[x] = new_board[x][:y]+'0' + new_board[x][y+1:]
        return 0

def changeboard(new_board, y, m,n) :
    chlist = list()
    j=m-1
    for i in range (0,m) :
        if new_board[j][y] !='0' :
            chlist.append(new_board[j][y])
        j= j-1
    for i in range (len(chlist),m) :
        chlist.append('0')
    j=m-1    
    chlist = chlist[::-1]

    for i in range(0,m) :
        new_board[i] = new_board[i][:y] + chlist[i] + new_board[i][y+1:]


def solution(m, n, board):
    answer = 0
    flag =0
    

    while True :       
        new_board = copy.deepcopy(board) 
        countboard = [[0 for col in range(n+1)] for row in range(m+1)] # 개수 새기 위함 이거 만드는거 조심좀 하자잉~~?
        flag = 0
        for i in range(0,m-1) :
             for j in range(0,n-1) :
                if board[i][j] == board[i+1][j] and board[i+1][j] == board[i+1][j+1] and board[i+1][j+1] == board[i][j+1] and board[i][j] != '0' :
                    answer = answer + cntboard(new_board,countboard,i,j)
                    answer = answer + cntboard(new_board,countboard,i+1,j)
                    answer = answer + cntboard(new_board,countboard,i,j+1)
                    answer = answer + cntboard(new_board,countboard,i+1,j+1)
                    flag =1
        if flag==1 :
            for i in range (0,n) :
                changeboard(new_board,i,m,n)
            board = copy.deepcopy(new_board) 
        
        else :
            break;
    print(answer)
    return answer


solution(8,2, ["FF", "AA", "CC", "AA", "AA", "CC", "DD", "FF"])