Python 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> @@ -1,6 +1,44 @@
... # 1. 스택 코드 짜기
... # 2. 메인 입력 코드 짜기
... # 3. 계산기 코드 짜기
... # 4. 예외처리
... # 5. 예외처리
... # 6. 이스터에그
... # 6. 이스터에그
... 
... #작성된 메인 함수 코드에서 그대로 수정 진행했습니다
... 
... 
... isError = False #ERROR 출력을 결정하는 변수입니다.
... 
... class Stack(): 
...     def insert(enrty):
...         return
... 
... def isDivision():
...     return 
... 
... def isInteger():
...     global = isError #isError 전역변수 참조
...     isError = True   #ERROR 출력을 위해 True로 값 변경
...     return False     #입력값은 정수가 아님      
... 
... def calculator():
...     return 
... 
... def main():
...     myStack = Stack()
... 
...     while True:
...         try:
...             entry = int(input("숫자 혹은 연산자를 입력하세요: ")) 
...         except ValueError:
...             isInteger() #정수가 아닌 숫자가 입력됐을때 isInteger 함수 실행
        if entry =='=': 
            if not isError:
                calculator()
            else:
                print("= ERROR!")

if __name__ == "__main__": 
