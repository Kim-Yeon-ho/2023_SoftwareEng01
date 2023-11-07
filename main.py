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
    
def isDivision():
    return #isError값 수정하고 불 반환

def isInteger():
    return #isError값 수정하고 불 반환

def calculator():
    return #스택을 이용한 결과 값

def main():
    #입력값(정상,오류)이 저장될 스택 객체 선언
    myStack = Stack()

    while True:
        try:
            entry = int(input("숫자 혹은 연산자를 입력하세요: ")) #entry변수로 사용자 입력을 저장
        except ValueError: #이 부분에서 isDivision, isInteger함수를 사용할 수 있습니다!

        if entry =='=': #entry가 '=' 이라면 해당 값 출력
            if not isError:
                calculator()
                    #이스터에그 출력 코드 작성해주세요
            else:
                print("= ERROR!")

if __name__ == "__main__": #파이썬에서 main함수를 실행하는 코드
    main()
        
        