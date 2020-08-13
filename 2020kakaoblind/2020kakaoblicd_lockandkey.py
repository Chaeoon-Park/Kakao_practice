
import copy

def rotate_90(m): 
    N = len(m)
    ret = [[0] * N for _ in range(N)] 
    for r in range(N):
         for c in range(N): 
             ret[c][N-1-r] = m[r][c] 

    return ret

def rotate_180(m): 
    N = len(m)
    ret = [[0] * N for _ in range(N)] 
    for r in range(N):
         for c in range(N): 
             ret[N-1-r][N-1-c] = m[r][c] 

    return ret

def rotate_270(m): 
    N = len(m)
    ret = [[0] * N for _ in range(N)] 
    for r in range(N):
         for c in range(N): 
             ret[N-1-c][r] = m[r][c] 

    return ret

def checker(chkey, chlock,x,y) :
    copylock = copy.deepcopy(chlock)
    for i in range(0,len(chkey)) :
        for j in range(0,len(chkey)) :
            if copylock[i+x][j+y] == 1 and chkey[i][j] ==1 :
                return False
            elif chkey[i][j] ==1 :
                copylock[i+x][j+y] = chkey[i][j]

    for i in range(len(chkey)-1 , len(copylock)-len(chkey)+1) :
        for j in range(len(chkey)-1 , len(copylock)-len(chkey)+1) :
            if copylock[i][j] == 0 :
                return False
    
    return True

def solution(key, lock):
    answer = False
    newlocklen = len(lock) + 2 * len(key) - 2
    newlock = [[0 for col in range(newlocklen)] for row in range(newlocklen)]

    keys = []
    keys.append(key)
    keys.append(rotate_90(key))
    keys.append(rotate_180(key))
    keys.append(rotate_270(key))

    for i in range(0,newlocklen) :
        for j in range(0,newlocklen) :
            if i>=len(key)-1 and i<=newlocklen - len(key) and j>=len(key)-1 and j<=newlocklen - len(key) :
                newlock[i][j] = lock[i-len(key) + 1][j-len(key) + 1]
            else :
                newlock[i][j]=0

    for i in range(0,len(key)+ len(lock) -1) :
        for j in range(0,len(key)+ len(lock) -1) :
            if i==3 and j==3 :
                i=i
            for k in range(0,4) :
                if checker(keys[k],newlock,i,j) == True :
                    answer =True
    
    print(answer)
    return answer


solution(	[[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]])