class Exercise5:

    def addition(self):
        numero = self.__number_input()
        numero = sum(numero)
        return f"El resultado de la suma de los números ingresados es: {numero}"

    def subtraction(self):
        numero = self.__number_input()
        numero = numero[0] - numero[1]
        return f"El resultado de la resta de los números ingresados es: {numero}"

    def multiplication(self):
        numero = self.__number_input()
        numero = numero[0] * numero[1]
        return f"El resultado de la multiplicación de los números ingresados es: {numero}"

    def division(self):
        numero = self.__number_input()
        numero = numero[0] // numero[1]
        return f"El resultado de la división de los números ingresados es: {numero}"

    def exponent(self):
        numero = self.__number_input()
        numero = pow(numero[0], numero[1])
        return f"El resultado de la elevación exponencial de los números ingresados es: {numero}"

    def remainder(self):
        numero = self.__number_input()
        numero = numero[0] % numero[1]
        return f"El resultado del módulo de los números ingresados es: {numero}"

    @staticmethod
    def __number_input():
        numero = [int(input("Ingrese el primer número: ")),
                  int(input("Ingrese el segundo número: "))]
        return numero
