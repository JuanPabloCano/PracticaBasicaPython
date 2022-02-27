from model.exercise5.service.Exercise5 import Exercise5


class Main:

    @classmethod
    def start(cls):
        cls.exercise_5_conditionals()

    @staticmethod
    def exercise_5_menu():
        print()
        print("***** Bienvenido a la calculadora de funciones aritméticas *****\n"
              "1. Suma\n"
              "2. Resta\n"
              "3. Multiplicación\n"
              "4. División\n"
              "5. Elevación exponencial\n"
              "6. Módulo\n"
              "7 .Salir\n"
              "Seleccione una opción: ")
        numero = int(input())
        return numero

    @staticmethod
    def exercise_5_conditionals():
        x = Exercise5()
        while True:
            numero = Main.exercise_5_menu()
            if numero == 1:
                print(x.addition())
            elif numero == 2:
                print(x.subtraction())
            elif numero == 3:
                print(x.multiplication())
            elif numero == 4:
                print(x.division())
            elif numero == 5:
                print(x.exponent())
            elif numero == 6:
                print(x.remainder())
            elif numero == 7:
                print("Hasta luego")
                break
            else:
                print("Solo se permite el ingreso de números del 1 al 7")
