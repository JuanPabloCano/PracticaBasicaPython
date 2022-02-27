class Exercise3:
    def __init__(self):
        self.nums = []

    def number_input(self, num1, num2, num3):
        self.__list_append(num1, num2, num3)
        maxim = max(self.nums)
        return f"El número {maxim} es el número más grande de los tres"

    def __list_append(self, num1, num2, num3):
        self.nums.append(num1)
        self.nums.append(num2)
        self.nums.append(num3)
