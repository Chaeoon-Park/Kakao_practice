
#Trie 꼭 꼭 다시. 중요함 아마 카카오에서 제일 중요

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
        for i in range (len(path)-1 , -1 , -1) : #끝난 단어의 길이 위치의 자식 수만 업데이트 하면 됨.
            
            if path[i].number.get(icnt) == None :
                path[i].number[icnt] = 1
            else :
                path[i].number[icnt] = path[i].number[icnt]  + 1
            icnt = icnt+1
        
        current_node.data = string

    def search(self, string) :
        current_node = self.head
        for char in string :
            if char == '?' : #이게 아니라 개수도 맞아야지 
                break
            elif char in current_node.children :
                current_node = current_node.children[char]
            else :
                return 0
        nums = string.count('?')
        if current_node.number.get(nums) == None :
            return 0
        else :
            return current_node.number.get(nums)



def solution(words, queries):
    answer = []
     #처음에 암것도 없는거 생성해야해

    trie = Trie()
    btrie = Trie()
    for word in words :
        trie.insert(word)
        btrie.insert(word[::-1])

    for querie in queries :
        if querie[0]=='?' :
            answer.append(btrie.search(querie[::-1]))           
        elif querie[len(querie)-1]=='?' :
            answer.append(trie.search(querie))         
    return answer

solution(	["frodo", "front", "frost", "frozen", "frame", "kakao"], ["fro??", "????o", "fr???", "fro???", "pro?"] )