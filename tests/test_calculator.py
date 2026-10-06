from app.tools.calculator import Calculator


calculator = Calculator()

print("10 - 3 =", calculator.subtract(10, 3))
print("10 + 3 =", calculator.add(10, 3))
print("Price difference =", calculator.percentage_difference(110, 100), "%")