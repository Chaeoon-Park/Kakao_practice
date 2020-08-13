global cnt
global banneds
global bcnt
global visit
class Node(object) :
    def __init__(self, key, data=None) :
        self.key = key
        self.data = data  #끝난거 알기 위해서 
        self.number = dict()
        self.children={} #자식 노드 싹싹 더하기
class Trie(object) :
    def __init__(self) :
        self.head= Node(None)
    def insert(self, string) :
        current_node = self.head
        path = []
        for char in string :
            if char not in current_node.children :
                current_node.children[char] = Node(char) #char가 배열 주소로 가능하다니 ; 이거 중요함
            path.append(current_node)
            current_node = current_node.children[char]
        icnt = 1
        for i in range (len(path)-1 , -1 , -1) : #끝난 단어의 길이 위치의 자식 수만 업데이트 하면 됨. 여기서 꼭 필요하진 않지만 ㅎㅎ
            
            if path[i].number.get(icnt) == None :
                path[i].number[icnt] = 1
            else :
                path[i].number[icnt] = path[i].number[icnt]  + 1
            icnt = icnt+1
        
        current_node.data = string

    def search(self, nownode, string, nowstring) :
        global cnt
        global banneds
        global bcnt
        current_node = nownode
        i = 0

        for char in nowstring :

            if char == '*' : 
                for child in current_node.children :
                    self.search(current_node.children[child],string, nowstring[i+1:])
                break
            elif char in current_node.children :
                current_node = current_node.children[char]
            else :
                return 0
            i= i+1
        if current_node.data != None and len(string) == len(current_node.data):
            banneds[bcnt].append(current_node.data)

def dfs(nowcnt, banneds, nowmap, n) :
    global visit
    if n==nowcnt :
        sum =0
        for i in nowmap :
            sum += pow(2,i)
        if visit[sum] == False :
            global cnt
            cnt = cnt +1
            visit[sum] = True

    else :
        for ban in banneds[nowcnt] :
            if ban not in nowmap :
                nowmap.append(ban)
                dfs(nowcnt+1, banneds,nowmap , n)
                nowmap.pop()


def solution(user_id, banned_id):
    answer = 0
    global cnt
    global banneds
    global bcnt
    global visit
    visit = [False for i in range(513)]
    banneds= [ [] for i in range(len(banned_id))]
    bcnt = 0
    cnt = 0
    trie = Trie()
    dic = dict()
    i=0
    for user in user_id :
        trie.insert(user)
        dic.update({user : i})
        i = i+1
    for banned in banned_id :
        trie.search(trie.head, banned, banned)
        bcnt = bcnt+1
    for banned in banneds :
        
        for i in range(len(banned)) :
            banned[i] = dic.get(banned[i])
    dfs(0,banneds,[],len(banned_id))
    

    answer = cnt
    return answer


solution(	["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*rodo", "*rodo", "******"])