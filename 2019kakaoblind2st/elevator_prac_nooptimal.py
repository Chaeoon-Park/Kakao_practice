import requests
import json
import math
import copy
url = 'http://localhost:8000'

#빌딩 배열은 넣을 때 체크를 해줘야함

class Elevator(object) :
  
    def __init__(self, id, floor, passengers, status) :
        self.id = id
        self.floor = floor
        self.passengers = passengers
        self.status = status
        self.destination = 1
        self.startfloor = 1
        self.endfloor = 25
        self.maxpeople = 8
        self.call_ids = [] #오류 나면 얘때문에 날거같음. 조심할 것
        self.command = "STOP"

    def change_state(self, floor, passengers, status) :
        self.floor = floor
        self.passengers = passengers
        self.status = status



    def checkmax(self) :
        if len(self.passengers)==self.maxpeople :
            return True
        else :
            return False
    
    def ch_destination(self,new_des) :
        # 더 높은곳
        if self.status == "UPWARD" and new_des > self.destination :
            self.destination = new_des
        # 더 낮은곳 
        elif self.status == "DOWNWARD" and new_des < self.destination :
            self.destination = new_des
        # 멈추고 더 낮은곳
        elif self.status == "STOPPED" and self.destination <= self.floor and new_des < self.floor and new_des < self.destination :
            self.destination = new_des
        # 멈추고 더 높은곳
        elif self.status == "STOPPED" and self.destination >= self.floor and new_des > self.floor and new_des > self.destination :
            self.destination = new_des

    def stopped_change(self) :
        #멈춰있을때만 작동해야함
        #반환값은 명령값
        if self.destination  != self.floor and self.destination > self.floor :
            self.command = "UP"
            return True

        elif self.destination  != self.floor and self.destination < self.floor :
            self.command = "DOWN"
            return True
        #목적지에 도달하고 멈춰있을 때 목적지 재설정
        elif self.destination == self.floor and len(self.passengers)>0 :
            d_point = 0
            min = 0
            for pas in self.passengers :
                if abs(pas['end'] - self.floor) > min :
                    min =  abs(pas['end'] - self.floor)
                    d_point = pas['end'] 
            
            if d_point > self.floor :
                self.destination = d_point
                self.command =  "UP"
                return True
            
            elif d_point < self.floor :
                self.destination = d_point
                self.command =  "DOWN"
                return True
        
        self.command =  "STOP"
        return False
            
    def leftchange(self) : 
        #운행가능 층수에 다 도달했는지 확인하는 기능
        if self.status == "DOWNWARD" and self.floor == self.startfloor :
            self.command =  "STOP"
            return True
        elif self.status == "UPWARD" and self.floor == self.endfloor :
            self.command = "STOP"
            return True
        else :
            return False

    
    def check_stop(self, bilding) :
        #상태가 opened이 아닐때만 하는 것이야 ~

        #내릴사람
        byids = []
        for pas in self.passengers :
            if pas['end'] == self.floor :
                byids.append(pas["id"])

        #탈사람
        enterids = []
        nowins = len(self.passengers)
        cnt = 0
        if len(bilding[self.floor]) != 0 :
            for guys in bilding[self.floor] :
                cnt = cnt + 1
                if cnt + nowins <= self.maxpeople :
                    enterids.append(guys["id"])
                else : 
                    break
        
        
        if (len(byids) > 0 or len(enterids) >0 ) and self.status != "STOPPED" and self.status != "OPENED" :  
            self.command = "STOP"
            return True 
        elif (len(byids) > 0 or len(enterids) >0 )  and self.status == "STOPPED" :
            self.command = "OPEN"
            return True
        
        return False
    
    def open_byebye(self, bilding) :

        #현재 상태가 열려있을때는 1.내릴사람이 있는지 먼저 체크. 있다면 내리는 작업 먼저 해야함
        byids = []
        for pas in self.passengers :
            if pas['end'] == self.floor :
                byids.append(pas["id"])
        if len(byids) > 0 :
            self.call_ids = copy.deepcopy(byids)
            self.command = "EXIT"
            return True
        

        #2. 내릴 사람이 없다면 탈사람이 있는지 체크 이거는 인원이 많으면 만원이 안 넘도록 조심해야함
        enterids = []
        nowins = len(self.passengers)
        cnt = 0
        if len(bilding[self.floor]) != 0 :
            for guys in bilding[self.floor] :
                cnt = cnt + 1
                if cnt + nowins <= self.maxpeople :
                    enterids.append(guys["id"])
                else : 
                    break
            if  len(enterids) > 0 :
                newfloor = []
                for guys in bilding[self.floor] :
                    if guys['id'] not in enterids :
                        newfloor.append(guys)

                self.call_ids = copy.deepcopy(enterids)
                bilding[self.floor] = copy.deepcopy(newfloor)
                self.command = "ENTER"
                return True
        
        #둘다 없으면 문 닫아버려
        self.command = "CLOSE"
        return True
            

    
        


def start(user_key,problem_id, number_of_elevators) :
    uri = url + '/start/' + user_key + '/' + str(problem_id) + '/' + str(number_of_elevators)
    return requests.post(uri).json()

def oncalls(token) :
    uri = url + '/oncalls'
    return requests.get(uri,headers = {'X-Auth-Token' : token }).json()

def action(token, cmds) :
    uri = url + '/action'
    header = {'X-Auth-Token' : token }
    js = {'commands' : cmds}
    return requests.post(uri, headers =  header , json = js ).json()




def simulator() :
    user = 'tester'
    problem = 2
    count = 4
    ret = start(user, problem, count)
    token = ret['token']
    print('Token for %s is %s' % (user, token))
    elevators = [{} for i in range(4)]
    for ele in ret['elevators'] :
        elevators[ele['id']] = Elevator(ele['id'],ele['floor'],ele['passengers'],ele['status'])

    is_end = False
    bilding = [ [] for i in range(50) ] #층수에 따라서 당연히 다르게 해야겠지?
    while is_end == False :
        ret = oncalls(token)
        for ele in ret['elevators'] :
            elevators[ele['id']].change_state(ele['floor'] , ele['passengers'] , ele['status'])
        # calls에 대한 처리는
        # 1. 이미 들어가있는 친구인지 봄
        for call in ret['calls'] :
            flag = False
            for people in bilding[call['start']] :
                if people['id'] == call['id'] :
                    flag = True


            # 2. 새로 들어가야하면 일단 건물에 넣음

            if flag == False :
                bilding[call['start']].append(call)


            # 3. 가장 가까운 엘리베이터 찾고, 목적지 갱신 시도 이거는 들어가든 말든 계속 하자 혹시 모르니까
            max = 99999999
            epoint = -1

            for ele in elevators :
                distance = abs(call['start'] - ele.floor)
                if call['start'] >  ele.floor and ele.status == "UPWARD" and distance < max:
                    max = distance
                    epoint = ele.id
                elif call['start'] <  ele.floor and ele.status == "DOWNWARD" and distance < max:
                    max = distance
                    epoint = ele.id
                elif ele.status == "STOPPED" and (ele.destination - ele.floor) * (ele.destination - call['start']) >=0 and distance < max :      
                    max = distance
                    epoint = ele.id
            if epoint !=-1 :
                elevators[epoint].ch_destination(call['start'])


        #call처리 끝나면 엘리베이터가 해야할 일을 쫙쫙쫙 시행함
        e_command = []
        for ele in elevators :
            newting = dict()
            flag = False
            if ele.status != "OPENED" :
                flag = ele.check_stop(bilding)
            
            if flag == False and ele.status == "OPENED" :
                flag = ele.open_byebye(bilding)

            if flag == False :
                flag = ele.leftchange()

            if flag == False and ele.status == "STOPPED" :
                flag = ele.stopped_change()

            newting.update({'elevator_id' : ele.id})
            newting.update({'command' : ele.command})
            if ele.command == "EXIT" or ele.command == "ENTER" :
                newting.update({'call_ids' : ele.call_ids })
            
            e_command.append(newting)
        
        a=1
        a=1
        a=1
        ret = action(token,e_command)

        is_end = ret['is_end']

if __name__ == '__main__':
    simulator()