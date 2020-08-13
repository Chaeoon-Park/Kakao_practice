
import collections as col


def plusdeq(visit, deq , x1,y1,x2,y2, bang, cnt) :
    if visit[x1][y1][x2][y2] > cnt  and visit[x2][y2][x1][y1] > cnt  :
        visit[x1][y1][x2][y2] = cnt
        visit[x2][y2][x1][y1] = cnt
        deq.append([[x1,y1],[x2,y2],bang,cnt])

def solution(board):
    answer = 999999
    deq = col.deque() #현재 위치랑 할 수 있는 방향    좌표 2개와 새로방향인지 가로방향인지 나타내준다.   0번지 좌표 x 1번지 좌표y 3번지 회전상태 0이 가로 1이 세로 4번지 움직인 회수

    deq.append([[0,0],[0,1],0,0])
    visit = [[[[99999 for col in range(len(board))] for row in range(len(board))] for third in range(len(board))] for forth in range(len(board))]  #넣을때 같이 있는 모양도 같이 넣고, 숫자도 넣을 것
    visit[0][0][0][1] = 0
    visit[0][1][0][0] = 0
    board.append([])
    

    for i in range(0,len(board)) :
        board[i].append(1)

    for i in range(0,len(board)) :
        board[len(board)-1].append(1)
    

    while len(deq)!=0 :
        now = deq.popleft() #큐로 사용할때
        pos1 = now[0]
        pos2 = now[1]
        bang = now[2]
        cnt = now[3]

        if pos1 == [len(board)-2, len(board)-2] or pos2 == [len(board)-2, len(board)-2] :
            if cnt<answer :
                answer = cnt
        else :
            if  board[pos1[0]+1][pos1[1]]==0 and board[pos2[0]+1][pos2[1]]==0 :
                plusdeq(visit,deq,pos1[0]+1,pos1[1],pos2[0]+1,pos2[1],bang, cnt+1 )
                if now[2] == 0 :

                    plusdeq(visit,deq,pos1[0],pos1[1],pos1[0]+1,pos1[1], 1, cnt+1 )
                    plusdeq(visit,deq,pos2[0],pos2[1],pos2[0]+1,pos2[1], 1 , cnt+1 )
            if  (pos1[0]>0 and pos2[0]>0) and board[pos1[0]-1][pos1[1]]==0 and board[pos2[0]-1][pos2[1]]==0 :
                
                plusdeq(visit,deq,pos1[0]-1,pos1[1],pos2[0]-1,pos2[1],bang, cnt+1 )
                if now[2] == 0 :
                    plusdeq(visit,deq,pos1[0],pos1[1],pos1[0]-1,pos1[1],1, cnt+1 )
                    plusdeq(visit,deq,pos2[0],pos2[1],pos2[0]-1,pos2[1],1, cnt+1 )

            if  board[pos1[0]][pos1[1]+1]==0 and board[pos2[0]][pos2[1]+1]==0 :
                
                plusdeq(visit,deq,pos1[0],pos1[1]+1,pos2[0],pos2[1]+1,bang, cnt+1 )
                if now[2] == 1 :
                    plusdeq(visit,deq,pos1[0],pos1[1],pos1[0],pos1[1]+1,0, cnt+1 )
                    plusdeq(visit,deq,pos2[0],pos2[1],pos2[0],pos2[1]+1,0, cnt+1 )

            if  (pos1[1]>0 and pos2[1]>0) and board[pos1[0]][pos1[1]-1]==0 and board[pos2[0]][pos2[1]-1]==0 :
        
                plusdeq(visit,deq,pos1[0],pos1[1]-1,pos2[0],pos2[1]-1,bang, cnt+1 )
                if now[2] == 1 :
                    plusdeq(visit,deq,pos1[0],pos1[1],pos1[0],pos1[1]-1,0, cnt+1 )
                    plusdeq(visit,deq,pos2[0],pos2[1],pos2[0],pos2[1]-1,0, cnt+1 )
    print(answer)
    return answer

solution([[0, 0, 0, 1, 1], [0, 0, 0, 1, 0], [0, 1, 0, 1, 1], [1, 1, 0, 0, 1], [0, 0, 0, 0, 0]])



                # #2가지로 회전 가능 pos1기준 
                # if visit[pos1[0]][pos1[1]][pos1[0]+1][pos1[1]] > cnt+1 and  visit[pos1[0]+1][pos1[1]][pos1[0]][pos1[1]] > cnt+1
                #       visit[pos1[0]][pos1[1]][pos1[0]+1][pos1[1]] = cnt+1
                #       visit[pos1[0]+1][pos1[1]][pos1[0]][pos1[1]] = cnt+1 
                #       deq.append([[pos1[0],pos1[1]],[pos1[0]+1,pos1[1]],(now[2]+1)%2,cnt+1])
                
                # #pos2 기준
                # if visit[pos2[0]][pos2[1]][pos2[0]+1][pos2[1]] > cnt+1 and  visit[pos2[0]+1][pos2[1]][pos2[0]][pos2[1]] > cnt+1
                #       visit[pos2[0]][pos2[1]][pos2[0]+1][pos2[1]] = cnt+1
                #       visit[pos2[0]+1][pos2[1]][pos2[0]][pos2[1]] = cnt+1 
                #       deq.append([[pos2[0],pos2[1]],[pos2[0]+1,pos2[1]],(now[2]+1)%2,cnt+1])