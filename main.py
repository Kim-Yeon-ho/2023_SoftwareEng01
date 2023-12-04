# 입력을 계산하여 반환하는 함수
def calculate(expression):
    try:
        return eval(expression)
    except Exception as e:
        return f"Error: {e}"

# 입력 == "/"인지 판별하는 함수
def isDivision(userInput):
    # 입력 == "/"이면 True반환, 아니면 False 반환
    return True if userInput == "/" else False

# 입력 == 실수형인지 판별하는 함수
def isFloat(userInput):
    try:
        float(userInput)
        return True
    except ValueError:
        return False


# 이스터에그 판별 후 string을 반환하는 함수
# 반환된 string은 main에서 출력됨.
def easterEgg(userInput):
    if userInput == "5252":
        return "정종욱 교수님을 총장으로"
    elif userInput == "1015":
        return "전북대 개교기념일입니다."
    else:
        return "Not App"


def main():
    expression = ""
    errorChecker = False

    while True:
        userInput = input().strip()
        # 입력을 easterEgg에 대입하여 값으로 반환받음
        # 즉, easterEggValue는 모종의 string
        easterEggValue = easterEgg(userInput)

        # 기존 isEqual함수 대체
        # input == "="인 경우 처리
        if userInput == "=":
            # 에러에 해당하는 입력이 있었을 경우 Error출력
            if errorChecker == True:
                print("Error")
            # 에러에 해당하는 입력이 없었다면 값 계산 후 출력
            # 출력한 후 break
            else:
                result = calculate(expression)
                print(f"{result}")
                break
        # 입력이 이스터에그에 해당하는지 확인
        # 분기문 진입 조건은 입력값이 easterEgg에 해당할 때
        # 즉, 입력값이 이스터에그에 해당하지 않는 경우가 아닐 때
        elif easterEggValue != "Not App":
            print(f"{easterEggValue}")
            break
        # 입력이 float이거나, division이면 에러 체크
        elif isFloat(userInput) or isDivision(userInput):
            errorChecker = True
        else:
            expression += userInput

if __name__ == "__main__":
    main()
