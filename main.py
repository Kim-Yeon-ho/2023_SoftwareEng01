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

    #reverses 함수 추가를 위해 추가함
    def reverses(self):
        self.stack.reverse()
        
isError = False #ERROR 출력을 결정하는 변수입니다.

def calculator(lst):
    lst.reverses()  # 입력받은 스택은 pop으로 꺼낼 시 역순으로 계산되므로 정방향 계산을 위해 reverse()함수사용

    formula = ""  # eval함수 사용을 위해 string값으로 선언

    while lst.isEmpty() == 0:
        formula = formula + str(lst.pop())

    return eval(formula)
    
def isDivision(inputStr): #연산자가 나눗셈인지
    if inputStr == "/":
        # 입력된 연산자가 "/"이면 True 반환
        return True
    else:
        return False

def isInteger(inputInt):         # 숫자가 정수인지 판별하는 함수
     try:
         num = int(inputInt)
         return True             # 매개변수가 정수로 변환되면 True
     except ValueError:
         return False            # 변환되지 않으면 정수가 아니므로 False

def easterEgg(): #이스터에그 출력 함수
    return

def isEqual(input, lst): #등호가 입력되면 계산 결과 출력(ERROR처리할게 생각보다 많아 따로 함수로 작성했습니다)
    if input == '=': #input이 '=' 이라면 결과 값 출력
                if not isError:
                    print(calculator(lst))
                    easterEgg() #이스터에그 함수는 구현하시기 편한대로 바꾸시면 됩니다
                    exit(0)
                else:
                    print("ERROR!")
                    exit(0)
    return None

def main():
    myStack = Stack() #입력값(정상,오류)이 저장될 스택 객체 선언
    global isError
    isError = False

    while True:
        inputInt = input() #정수 입력
        if(isInteger(inputInt)):
            myStack.push(int(inputInt))
        else:
            isError = True
            isEqual(inputInt, myStack) #"3 + =" ERROR처리
        
        inputStr = input() #연산기호 입력 
        if(not isDivision(inputStr)):
            isEqual(inputStr, myStack) #연산자 +, *, -, = 중 =이 입력됐다면 결과 출력 
            myStack.push(inputStr) 
        else:
            isError = True
        
if __name__ == "__main__": #파이썬에서 main함수를 실행하는 코드
    main()
