import math
import unittest

def calculate(expression):
    try:
        return eval(expression)
    except Exception as e:
        return f"Error: {e}"

def isDivision(userInput):
    if userInput in ("+", "-", "*"):
        return False
    elif userInput == '/':      #10번 줄 없애도 됨
        return True             #11번 줄 없애도 됨
    return True

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

def factorial(expression):
    if len(str(expression).split()) > 1:
        return "[ERROR] Input Error"
    expressionStriped = expression.strip()
    if not str(expressionStriped).isdigit():
        return "[ERROR] Out Of Range"
    return "=" + str(math.factorial(int(expressionStriped)))

class TestFactorialFunction(unittest.TestCase):
    def testMultiple(self):
        self.assertEqual(factorial("3 3"),"[ERROR] Input Error")
        self.assertEqual(factorial("4 4 4"),"[ERROR] Input Error")
    def testPositive(self):
        self.assertEqual(factorial('5'),"=120")
    def testZero(self):
        self.assertEqual(factorial('0'),"=1")
    def testNegative(self):
        self.assertEqual(factorial('-1'),"[ERROR] Out Of Range")
    def testNoneInteger(self):
       self.assertEqual(factorial('+'),"[ERROR] Out Of Range")
       self.assertEqual(factorial('a'),"[ERROR] Out Of Range")
       self.assertEqual(factorial('0.1'),"[ERROR] Out Of Range")

def main():
    expression = ""
    errorChecker = False
    compare = 0     #피연산자와 연산사 가려주는 변수

    while True:
        userInput = input().strip()
        easterEggValue = easterEgg(userInput)
        compare+=1

        if userInput == "=":
            # 주석해제하여 체크 / print(f"exp: {expression}\nerrChecker: {errorChecker}")
            if errorChecker == True:
                print("[SYSTEM] \"Error!\"")
                break

            else:
                result = calculate(expression)
                print(f"{result}")
                break
        elif easterEggValue != "Not App":
            print(f"[EVENT] \"{easterEggValue}\"")
            break
        if userInput == "!":
            print(factorial(expression))
            
            break

        #elif isFloat(userInput) or isDivision(userInput):
        #   errorChecker = True
        else:
            if compare % 2: #정수 입력
                if isFloat(userInput):
                    errorChecker = True
            elif not (compare % 2): #연산자 입력
                if isDivision(userInput):
                    errorChecker = True
            # 주석해제하여 체크 / print(f"before add: {expression}")
            expression += userInput + " "  
            # 주석해제하여 체크 / print(f"after add: {expression}")
if __name__ == "__main__":
    unittest.main()
    #main()
