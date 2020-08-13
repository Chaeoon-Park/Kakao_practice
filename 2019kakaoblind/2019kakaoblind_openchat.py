def solution(records):
    answer = []
    dic = dict()
    for record in records :
        record = record.split(' ')
        if record[0]=='Enter' :
            dic.update({record[1] : record[2]})
        elif record[0] == 'Leave' :
            record[0] = record[0]
        elif record[0] == 'Change' :
            dic.update({record[1] : record[2]})
    for record in records :
        record = record.split(' ')
        if record[0]=='Enter' :
            answer.append(dic.get(record[1]) + "님이 들어왔습니다.")
        elif record[0] == 'Leave' :
            answer.append(dic.get(record[1]) + "님이 나갔습니다.")
    return answer

solution	(["Enter uid1234 Muzi", "Enter uid4567 Prodo", "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"])