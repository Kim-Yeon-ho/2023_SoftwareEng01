# 1. 스택 코드 짜기
# 2. 메인 입력 코드 짜기
# 3. 계산기 코드 짜기
# 4. 예외처리
# 5. 예외처리
# 6. 이스터에그

def isInteger(userInput):
    # 정수 or 실수 예외처리 필요
    return False
    
def isDivision(userInput):
    if userInput == "/":
        return True
    else:
        return False

def main():
    errChecker = False
    result = ""

    while True:
        userInput = input("Input: ")

        if isDivision(userInput):
            errChecker = True
        elif userInput == "=":
            if errChecker == False:
                result = eval(result)
                break
            else:
                result = "Error"
                break
        else:
            result +=userInput
    
    print(f"Result: {result}")

if __name__ == "__main__":
    main()