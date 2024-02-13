class Calculator:
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        return x / y


calculator = Calculator()

num1 = float(input())
num2 = float(input())

print(calculator.add(num1, num2))
print(calculator.subtract(num1, num2))
print(calculator.multiply(num1, num2))
print(calculator.divide(num1, num2))
