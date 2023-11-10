Python 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # 1. 스택 코드 짜기
... # 3. 계산기 코드 짜기
... # 4. 예외처리
... # 5. 예외처리
... # 6. 이스터에그
... 
... #메인함수에 사용될 사용자 정의 함수들의 이름을 간략하게 지었습니다.
... #고쳐쓰시면 됩니다!!!
... 
... isError = False #ERROR 출력을 결정하는 변수입니다.
... 
... class Stack():                      
...     def __init__(self):             
...         self.stack = []
...     
...     def push(self, data):           
...         self.stack.append(data)     
...     
...     def pop(self):                  
...         popObject = None
...         if self.isEmpty():         
...             return False
...         else:
...             popObject = self.stack.pop()
...         
...         return popObject
...     
...     def top(self):                  
...         topObject = None
...         if self.isEmpty():          
...             return False
...         else:
...             topObject = self.stack[-1]
...         
...         return topObject 
...     
...     def isEmpty(self):              
        isEmpty = False
        if len(self.stack) == 0:
            isEmpty = True
        
        return isEmpty
    
def isDivision(inputStr): 
    return 

def isInteger(inputInt):            #숫자가 정수인지 판별하는 함수
...     try:                        
...         num = int(inputInt)     
...         return True             #매개변수가 정수로 변환되면 True
...     except ValueError:
...         return False            #변환되지 않으면 정수가 아니므로 False

def calculator():
    return 

def isEqual(input): 
    if input == '=': 
                if not isError:
                    calculator()
                    exit(0)
                else:
                    print("= ERROR!")
                    exit(0)
    return None

def main():
    myStack = Stack() 

    while True:
        inputInt = input() #정수 입력
        if(isInteger(inputInt)):
            myStack.push(inputInt)
        else:
            isError = True
            isEqual(inputInt)
        
        inputStr = input() 
        if(not isDivision(inputStr)):
            isEqual(inputStr)
            myStack.push(inputStr)
        else:
            isError = True
            isEqual(inputStr)
        
if __name__ == "__main__": 
