def calculate(expression):
    try:
        return eval(expression)
    except Exception as e:
        return f"Error: {e}"

def isDivision(userInput):
    if userInput == "/":
        return True
    elif userInput == "+" or "-" or "*":
        return False

def isFloat(userInput):
    if "." in userInput:
        try:
            float(userInput)
            return True
        except ValueError:
            return False
    return False

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
        easterEggValue = easterEgg(userInput)

        if userInput == "=":
            # 주석해제하여 체크 / print(f"exp: {expression}\nerrChecker: {errorChecker}")
            if errorChecker == True:
                print("Error")
            else:
                result = calculate(expression)
                print(f"{result}")
                break
        elif easterEggValue != "Not App":
            print(f"{easterEggValue}")
            break
        elif isFloat(userInput) or isDivision(userInput):
            errorChecker = True
        else:
            # 주석해제하여 체크 / print(f"before add: {expression}")
            expression += userInput
            # 주석해제하여 체크 / print(f"after add: {expression}")
if __name__ == "__main__":
    main()
