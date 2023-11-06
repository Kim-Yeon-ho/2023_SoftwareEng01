# 1. 스택 코드 짜기
# 2. 메인 입력 코드 짜기
# 3. 계산기 코드 짜기
# 4. 예외처리
# 5. 예외처리
# 6. 이스터에그
 

class Stack():                      #Stack 클래스 생성
    def __init__(self):             #클래스 초기화
        self.stack = []
    
    def push(self, data):           #스택에 데이터 추가
        self.stack.append(data)     
    
    def pop(self):                  #스택에서 데이터 반환
        popObject = None
        if self.isEmpty():         
            print("Stack is Empty")
        else:
            popOjbect = self.stack.pop()
        
        return popObject
    
    def top(self):                  #스택의 가장 위에 있는 데이터 반환
        topObject = None
        if self.isEmpty():
            print("Stack is Empty")
        else:
            topObject = self.stack[-1]
        
        return topObject 
    
    def isEmpty(self):              #스택이 비어있으면 True, 채워져있으면 False
        isEmpty = False
        if len(self.stack) == 0:
            isEmpty = True
        
        return isEmpty



class Node:                         #Linked list를 위한 Node 클래스 생성
    def __init__(self, data):
        self.data = data
        self.next = None

class linkedListStack():            #linkedListStack 클래스 생성
    def __init__(self):             #클래스 초기화
        self.head = None
    
    def push(self, data):           #스택에 데이터 추가
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode
    
    def pop(self):                  #스택에서 데이터 반환
        popObject = None

        if self.isEmpty():
            print("Stack is Empty")
        else:
            popObject = self.head.data
            self.head = self.head.next
        
        return popObject
    
    def top(self):                  #스택의 가장 위에 있는 데이터 반환
        topObject = None
        if self.isEmpty():
            print("stack is Empty")
        else:
            topObject = self.head.data
        
        return topObject
    
    def isEmpty(self):              #스택이 비어있으면 True, 채워져있으면 False
        isEmpty = False
        if self.head is None:
            isEmpty = True
        
        return isEmpty
 