
#현재 구조가 가능한지 확인하는 친구
global lenn
def xtest(structure , x, y) :
    global lenn
    n = lenn

    if x>n or y>n or x<0 or y<0:
        return 1  
    else :
        if structure[0][x][y]==1 :
            if (y==0) or (x>0 and structure[1][x-1][y] ==1) or (structure[1][x][y] ==1) or (y>0 and structure[0][x][y-1] ==1) :
                x=x
            else :
                return 0
        if structure[1][x][y]==1 :
            if (y>0 and structure[0][x][y-1] ==1) or (x>0 and structure[1][x-1][y] ==1 and structure[1][x+1][y] ==1) or (y>0 and structure[0][x+1][y-1] ==1)  :
                x=x
            else :
                return 0
    return 1


def solution(n, build_frame):
    answer = []
    structure = [[[0 for i in range(0,n+1)] for j in range(0,n+1)] for k in range(2)]
    global lenn
    lenn=n
    for build in build_frame :
        if build[0]== 1 and build[1] == 1 and build[2] ==1 :
            n=n

        if build[3] == 0 :
            structure[build[2]][build[0]][build[1]] = 0
            flag = 0 
            for i in range(0,n+1) :
                for j in range(0,n+1) :
                    if xtest(structure,i,j)==0 :
                        flag = 1
                        break

            # if xtest(structure,build[0],build[1]+1) == 1 and xtest(structure,build[0]-1,build[1]) == 1 and xtest(structure,build[0]+1,build[1]) == 1 and xtest(structure,build[0],build[1]) == 1  and xtest(structure,build[0]+1,build[1]+1) == 1 and xtest(structure,build[0]-1,build[1]-1) == 1 :
            #     structure[build[2]][build[0]][build[1]] = 0
            if flag==1 :
                structure[build[2]][build[0]][build[1]] = 1

        else :
            structure[build[2]][build[0]][build[1]] = 1
            flag = 0 
            for i in range(0,n+1) :
                for j in range(0,n+1) :
                    if xtest(structure,i,j)==0 :
                        flag = 1
                        break
            if flag==1 :
                structure[build[2]][build[0]][build[1]] = 0


    for i in range (0,n+1) :
        for j in range(0,n+1) :
            if structure[0][i][j] == 1 :
                answer.append([i,j,0])
            if structure[1][i][j] == 1 :
                answer.append([i,j,1])    
    return answer

solution(		5, [[0, 0, 0, 1], [2, 0, 0, 1], [4, 0, 0, 1], [0, 1, 1, 1], [1, 1, 1, 1], [2, 1, 1, 1], [3, 1, 1, 1], [2, 0, 0, 0], [1, 1, 1, 0], [2, 2, 0, 1]])