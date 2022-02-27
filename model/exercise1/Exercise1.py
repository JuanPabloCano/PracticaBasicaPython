class Exercise1:

    def __init__(self):
        self.num = int(input("Ingrese un número: "))

    def isNumberOddOrEven(self):
        if self.num % 2 == 0:
            return f"El número {self.num} es par"
        return f"El número {self.num} es impar"
