class Stack():                      #Stack 클래스 생성
    def __init__(self):             #클래스 초기화
        self.stack = []
    
    def push(self, data):           #스택에 데이터 추가
        self.stack.append(data)     
    
    def pop(self):                  #스택에서 데이터 반환
        popObject = None
        if self.isEmpty():         #스택이 비어있으면 False, 있으면 반환
            return False
        else:
            popObject = self.stack.pop()
        
        return popObject
    
    def top(self):                  #스택의 가장 위에 있는 데이터 반환
        topObject = None
        if self.isEmpty():          #스택 최상단이 비어있으면 False, 있으면 반환
            return False
        else:
            topObject = self.stack[-1]
        
        return topObject 
    
    def isEmpty(self):              #스택이 비어있으면 True, 채워져있으면 False
        isEmpty = False
        if len(self.stack) == 0:
            isEmpty = True
        
        return isEmpty

def calculator(Objtest):
    
    stack = Objtest
    postList = []
    opStack = Stack()
    
    prior = {'*':2, '+':1, '-':1}
    
    for i in range(len(stack)):
        if stack[i].isdigit():
            postList.append(stack[i])
        else:
            while (not opStack.isEmpty() and prior[opStack.top()] >= prior[stack[i]]):
                postList.append(opStack.pop())
            