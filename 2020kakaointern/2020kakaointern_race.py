import collections as col
def solution(board):
    answer = 0
    # 현재 위치와 온쪽 방향을 가지고 있으면 될것 방향 바뀔시 500원 추가
    # 가격 맵을 만들어서 가격이 갱신할것
    # 경로 찾기는 무조건 bfs부터 생각하세요

    D = [[99999999 for i in range(len(board))] for j in range(len(board))]
    D[0][0]=0
    deq = col.deque()
    deq.append([0,0,0,0]) #번지수  [x,y,cost,방향 0 가로 1 세로] 
    deq.append([0,0,0,1]) #번지수  [x,y,cost,방향 0 가로 1 세로]    
    go_dirs = [ [1,0,0],[-1,0,0],[0,1,1],[0,-1,1] ]

    while len(deq)!=0 :
        im = deq.popleft()
        x = im[0]
        y = im[1]
        cost = im[2]
        dir = im[3]
        for go_dir in go_dirs :
            if x+go_dir[0] >=0 and x+go_dir[0] < len(board) and y+go_dir[1] >=0 and y+go_dir[1] < len(board) :
                
                roadcost = 100
                if go_dir[2] != dir :
                    roadcost = roadcost + 500

                if board[x+go_dir[0]][y+go_dir[1]] == 0 and D[x+go_dir[0]][y+go_dir[1]] >= cost + roadcost :
                         D[x+go_dir[0]][y+go_dir[1]] = roadcost + cost
                         deq.append([x+go_dir[0],y+go_dir[1],roadcost + cost, go_dir[2] ])
    
    answer = D[len(D)-1][len(D)-1]
    print(answer)
    return answer

solution([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
