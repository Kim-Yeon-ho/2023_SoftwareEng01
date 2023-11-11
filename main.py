# 1. 스택 코드 짜기
# 3. 계산기 코드 짜기
# 4. 예외처리
# 5. 예외처리
# 6. 이스터에그

#메인함수에 사용될 사용자 정의 함수들의 이름을 간략하게 지었습니다.
#고쳐쓰시면 됩니다!!!

isError = False #ERROR 출력을 결정하는 변수입니다.

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
    
def isDivision(inputStr): #연산자가 나눗셈인지
    return 

def isInteger(inputInt): #숫자가 정수인지
    return 

def easterEgg(): #이스터에그 출력 함수
    return

def calculator():
    return #스택을 이용한 결과 값

def isEqual(input): #등호가 입력되면 계산 결과 출력(ERROR처리할게 생각보다 많아 따로 함수로 작성했습니다)
    if input == '=': #input이 '=' 이라면 결과 값 출력
                if not isError:
                    calculator() 
                    easterEgg() #이스터에그 함수는 구현하시기 편한대로 바꾸시면 됩니다
                    exit(0)
                else:
                    print("= ERROR!")
                    exit(0)
    return None

def main():
    myStack = Stack() #입력값(정상,오류)이 저장될 스택 객체 선언

    while True:
        inputInt = input() #정수 입력
        if(isInteger(inputInt)):
            myStack.push(inputInt)
        else:
            isError = True
            isEqual(inputInt) #"3 + =" ERROR처리
        
        inputStr = input() #연산기호 입력 
        if(not isDivision(inputStr)):
            isEqual(inputStr) #연산자 +, *, -, = 중 =이 입력됐다면 결과 출력 
            myStack.push(inputStr) 
        else:
            isError = True
        
if __name__ == "__main__": #파이썬에서 main함수를 실행하는 코드
    main()
