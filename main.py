# 1. 스택 코드 짜기
# 2. 메인 입력 코드 짜기
# 3. 계산기 코드 짜기
# 4. 예외처리
# 5. 예외처리
# 6. 이스터에그

isError = False #ERROR 출력을 결정하는 변수입니다.

def isDivision(userInput):
     # 나눗셈 예외처리 필요
     return False

def isInteger(inputInt):         # 숫자가 정수인지 판별하는 함수
     try:
         num = int(inputInt)
         return True             # 매개변수가 정수로 변환되면 True
     except ValueError:
         return False            # 변환되지 않으면 정수가 아니므로 False
         
def main():
    myStack = Stack()            # 스택 함수 구현 필요

    while True:
        inputInt = input()       # 정수 입력
        if(isInteger(inputInt)):
            myStack.push(inputInt)
        else:
            isError = True
            isEqual(inputInt)    #"3 + =" ERROR처리
        
        inputStr = input()       # 연산기호 입력
        if(not isDivision(inputStr)):
            isEqual(inputStr)
            myStack.push(inputStr)
        else:
            isError = True
        
if __name__ == "__main__":
