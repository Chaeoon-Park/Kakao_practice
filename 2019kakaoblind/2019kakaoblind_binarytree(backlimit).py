import collections as col
import sys
sys.setrecursionlimit(10**6) #파이썬 재귀 제한 회수 1000. 재귀 제한 회수를 늘려줌. 이거 중요하다.
class Node(object) :
    def __init__(self, key, x, y) :
        self.key = key
        self.x = x
        self.y = y
        self.left = None
        self.right = None
class Tree(object) :
    def __init__(self) :
        self.head= Node(0,1000001,1000001)
    def insert(self, x, y, k) :
        current_node = self.head
        while True :
            if x<current_node.x and current_node.left == None :
                newnode= Node(k,x,y)
                current_node.left = newnode
                break
            elif x<current_node.x and current_node.left != None :
                current_node = current_node.left
            elif x>current_node.x and current_node.right == None :
                newnode= Node(k,x,y)
                current_node.right = newnode
                break
            elif x>current_node.x and current_node.right != None :
                current_node = current_node.right

    def preorder(self) :
          
        deq = col.deque()
        deq.append(self.head)
        pres =[]
        while len(deq)!=0 :
            current_node = deq.pop()
            if current_node.key != 0 :
                pres.append(current_node.key)
            if current_node.right != None :
                deq.append(current_node.right)
            if current_node.left != None :
                deq.append(current_node.left)
        return pres

global postpres

def postorder(tree, nownode) :
        if nownode.left != None :
            postorder(tree, nownode.left)
        if nownode.right != None :
            postorder(tree, nownode.right)
        if nownode.key!= 0 :
            global postpres
            postpres.append(nownode.key)

def solution(nodeinfo):
    answer = []

    cnt = 1
    for nos in nodeinfo :
        nos.append(cnt)
        cnt = cnt+1
    nodeinfo.sort(key = lambda x : (-x[1], x[0]))
    tree = Tree()
    for nos in nodeinfo :
        tree.insert(nos[0],nos[1],nos[2])
    answer.append(tree.preorder())
    global postpres
    postpres= []
    postorder(tree,tree.head)

    answer.append(postpres)

    return answer


solution([[0, 0] , [100000,100000]])