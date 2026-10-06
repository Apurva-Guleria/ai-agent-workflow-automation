class Calculator:

    def subtract(self, a, b):
        return a - b

    def add(self, a, b):
        return a + b

    def percentage_difference(self, a, b):
        if b == 0:
            raise ValueError("Cannot calculate percentage difference with zero.")

        return abs(a - b) / b * 100