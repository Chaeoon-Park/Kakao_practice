#우선순위 큐 사용 굉장히 중요
#이문제가 가장 몰랐던 문제인듯

from queue import PriorityQueue


def solution(food_times, k):
    
    if sum(food_times) <= k :
        return -1
    answer = 0
    q = PriorityQueue()
    for i in range(len(food_times)) :
        q.put((food_times[i], i+1)) #넣는것은 put 으로 넣을 것
    #알아서 소팅 되나? 첫번째거 기준으로?

    sum_value = 0 #누적 값
    past_value = 0 #이전값
    length = len(food_times)
    
    while sum_value + (q.queue[0][0] - past_value) * length <= k : #호출은 queue로 할 것
        now = q.get()[0] #get 하면 알아서 제일 작은것을 pop해줌. 들어가는 순서는 그냥 들어가고 get 했을때 가장 작은게 나오는게 큰 특징
        sum_value = sum_value + (now - past_value) * length
        length = length -1
        past_value = now
    
    result = sorted(q.queue , key = lambda x:x[1]) #처음에 음식 순서를 정해서 다시 정렬함으로서 순서를 알 수 있는게 포인트 아이디어.
    return result[(k-sum_value) % len(q.queue)][1]

solution(	[3, 1, 2], 5)


# 아니 링크드 리스트 직접 구현했더니 틀리네

# import copy


# class Node(object) :
#     def __init__(self, key, value, next, past) :
#         self.key = key
#         self.value = value
#         self.next = next
#         self.past = past


# def solution(food_times, k):
#     answer = -1
#     Llist = []
  
#     mintime = copy.deepcopy(food_times)
#     mintime.sort()
#     longtime = 0
#     cnt = len(food_times)
#     for i in range(0,len(food_times)) :
#         Llist.append(Node(i+1,food_times[i],None,None))
#         if i>0 :
#             Llist[i-1].next = Llist[i]
#             Llist[i].past = Llist[i-1]

#     Llist[len(food_times)-1].next  = Llist[0] 
#     Llist[0].past = Llist[len(food_times)-1]


#     now = Llist[0]
#     startkey = now.key #이거 바뀌면 카피로 해야할듯


#     for mt in mintime :
#         fminu = mt - longtime
#         if fminu > 0 and k - cnt*fminu >= 0 :
#             icnt = cnt
#             flag = 1
#             while True :
#                 now.value = now.value - fminu
#                 if now.value==0 :
#                     cnt = cnt-1
#                     (now.past).next = now.next
#                     (now.next).past = now.past
#                     if startkey == now.key :
#                         startkey = (now.next).key
#                         flag = 0

#                 now = now.next
#                 if now.key == startkey and flag ==1:
#                     break
#                 else :
#                     flag =1
#             k = k - icnt*fminu
#             longtime =mt
#         elif fminu > 0 and k - cnt*fminu < 0 :
#             mok = k%cnt
#             for i in range(0,mok) :
#                 now = now.next
#             answer = now.key
#             break

#     print(answer)
#     return answer

# 
# solution([1, 2, 3, 4, 5, 6], 15)
