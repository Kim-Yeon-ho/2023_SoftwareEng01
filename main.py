import unittest
import math

class TestOperation(unittest.TestCase):             # isDivision Test-Case
    def testAdditionCase(self):
        self.assertEqual(isDivision("+"), False)
    
    def testSubtractionCase(self):
        self.assertEqual(isDivision("-"), False)
    
    def testMultiplicationCase(self):
        self.assertEqual(isDivision("*"), False)

    def testDivisionCase(self):
        self.assertEqual(isDivision("/"), True)

class TestNumber(unittest.TestCase):                # isFloat Test-Case
    def testInteger(self):
        self.assertEqual(isFloat("10"), False)
    
    def testFloat(self):
        self.assertEqual(isFloat("10.52"), True)

class TestEasterEgg(unittest.TestCase):             # easterEgg Test-Case       
    def test5252(self):
        self.assertEqual(easterEgg("5252"), "정종욱 교수님을 총장으로")
    
    def test1015(self):
        self.assertEqual(easterEgg("1015"), "전북대 개교기념일입니다.")
        
### TDD: Factorial Function
class TestFactorialFunction(unittest.TestCase):     # Factorial Test-Case
    def testMultiple(self):
        self.assertEqual(factorial("3 3"), "[ERROR] Input Error")
        self.assertEqual(factorial("4 4 4"), "[ERROR] Input Error")

    def testPositive(self):
        self.assertEqual(factorial("5"), "= 120")

    def testZero(self):
        self.assertEqual(factorial("0"), "= 1")

    def testNegative(self):
        self.assertEqual(factorial("-1"), "[ERROR] Out Of Range")

    def testNoneInteger(self):
        self.assertEqual(factorial('+'), "[ERROR] Out Of Range")
        self.assertEqual(factorial('a'), "[ERROR] Out Of Range")
        self.assertEqual(factorial('0.1'), "[ERROR] Out Of Range")

def calculate(expression):                          # +, -, * 연산 함수
    try:                                            # string타입 expression을 eval함수로 계산
        return eval(expression)
    except Exception as e:
        return f"Error: {e}"

def isDivision(userInput):                          # "/" 입력 예외처리 함수
    if userInput in ("+", "-", "*"):
        return False
    elif userInput == '/':                          # "/" 가 입력되면 True 반환
        return True  
    return True

def isFloat(userInput):                             # 실수형 입력 예외처리 함수
    if "." in userInput:                            # 입력값에 "."이 포함될 경우 실수로 간주
        try:
            float(userInput)                           
            return True                             # 실수형이 입력되면 True 반환
        except ValueError:
            return False
    return False

def easterEgg(userInput):                           # 이스터에그 함수
    if userInput == "5252":
        return "정종욱 교수님을 총장으로"             # eaterEgg에 해당하는 string을 반환
    elif userInput == "1015":
        return "전북대 개교기념일입니다."
    else:
        return "Not App"

def factorial(expression):                          # factorial 함수
    if len(str(expression).split()) > 1:            # 숫자 연속입력 처리
        return "[ERROR] Input Error"                
    expressionStriped = expression.strip()          # 공백란 처리
    if not str(expressionStriped).isdigit():        # 음수 처리
        return "[ERROR] Out Of Range"
    return "= " + str(math.factorial(int(expressionStriped)))   

def main():
    expression = ""
    errorChecker = False
    compare = 0 

    while True:
        userInput = input().strip()
        easterEggValue = easterEgg(userInput)       # eaterEgg의 경우 입력시 바로 종료하기 위해 분기문 밖에 배치               
        compare += 1                                # 정수/연산자 입력 구분용 변수

        if userInput == "=":
            if errorChecker == True:
                print("[SYSTEM] ERROR!")            # 출력형식 수정: [SYSTEM] "Error!" -> [SYSTEM] ERROR!
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
        else:
            if compare % 2:  # 정수 입력
                if isFloat(userInput):
                    errorChecker = True
            elif not (compare % 2):  # 연산자 입력
                if isDivision(userInput):
                    errorChecker = True
            expression += userInput + " "

if __name__ == "__main__":
    unittest.main(exit=False)
    main()
