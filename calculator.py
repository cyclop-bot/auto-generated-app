class Calculator:
    def add(self, num1, num2):
        return num1 + num2
    def subtract(self, num1, num2):
        return num1 - num2
    def multiply(self, num1, num2):
        return num1 * num2
    def divide(self, num1, num2):
        if num2 == 0:
            return 'Cannot divide by zero'
        else:
            return num1 / num2

calc = Calculator()
print(calc.add(5, 3))
print(calc.subtract(10, 4))
print(calc.multiply(7, 2))
print(calc.divide(20, 4))