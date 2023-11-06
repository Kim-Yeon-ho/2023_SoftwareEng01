# 1. 스택 코드 짜기
# 3. 계산기 코드 짜기
# 4. 예외처리
# 5. 예외처리
# 6. 이스터에그

#메인함수에 사용될 사용자 정의 함수들의 이름을 간략하게 지었습니다.
#고쳐쓰시면 됩니다!!!

isError = False #ERROR 출력을 결정하는 변수입니다.

class Stack(): #정상 입력값을 저장하는 Stack 클래스 입니다.
    def insert(enrty):
        return

class ErrorStack(): #에러 입력값을 저장하는 Stack 클래스 입니다.
    def insert(enrty):
        return

def isDivision():
    return #isError값 수정

def isInteger():
    return #isError값 수정

def calculator():
    return #스택을 이용한 결과 값

def Main():
    while True:
        entry = input("숫자 혹은 연산자를 입력하세요: ")
        Stack = myStack
        Stack = myErrorStack
        
        
        if entry=='=':
            if not isError:
                calculator()
                    #이스터에그 처리
            else:
                print("= ERROR!")
        if isDivision(entry)&isInteger(entry):
            myStack.insert(entry)
        else:
            myErrorStack.insert(entry)
        
        
        