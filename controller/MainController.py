from model.exercise1.Exercise1 import Exercise1
from model.exercise2.Exercise2 import Exercise2
from model.exercise4.Exercise4 import Fibonacci
from model.exercise3.Exercise3 import Exercise3
from model.exercise5.view.Exercise_5_view import Main


class MainController:

    @classmethod
    def start(cls):
        while True:

            print()
            print()

            selection = MainController.main_menu()

            if selection == 1:
                x = Exercise1()
                print(x.isNumberOddOrEven())
            elif selection == 2:
                a, b, c = cls.exercise_2_input()
                x = Exercise2(a, b, c)
                print(x.vacation_days())
            elif selection == 3:
                num1, num2, num3 = cls.exercise_3_input()
                x = Exercise3()
                print(x.number_input(num1, num2, num3))
            elif selection == 4:
                x = Fibonacci()
                for i in range(18):
                    print(x.fibonacci_sequence(i), end=" ")
            elif selection == 5:
                Main.start()
            elif selection == 6:
                print("Muchas gracias por utilizar nuestros servicios, hasta la próxima")
                break

    @classmethod
    def exercise_3_input(cls):
        print("Ingrese 3 números")
        num1 = int(input())
        num2 = int(input())
        num3 = int(input())
        return num1, num2, num3

    @classmethod
    def exercise_2_input(cls):
        a = input("Ingrese su nombre: ")
        b = int(input("Ingrese la clave del departamento: "))
        c = int(input("Ingrese los años trabajados: "))
        return a, b, c

    @staticmethod
    def main_menu():
        print("Bienvenido al menú interactivo, por favor seleccione una opción:\n"
              "1. Validar si un número es par o impar\n"
              "2. Solicite sus días de vacaciones\n"
              "3. Ingrese 3 números y valide cuál es el más grande\n"
              "4. Conozca la suceción de Fibonacci\n"
              "5. Calculadora\n"
              "6. Salir\n")
        selection = int(input("Escriba aquí... "))
        return selection
