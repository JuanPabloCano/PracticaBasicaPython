class Exercise2:

    def __init__(self, name, department_key, years):
        self.name = name
        self.department_key = department_key
        self.years = years
        self.vacation = 0

    def vacation_days(self):
        if self.department_key == 1:
            if self.years == 1:
                self.vacation = 6
                return self.__message()
            elif 2 <= self.years <= 6:
                self.vacation = 14
                return self.__message()
            elif self.years >= 7:
                self.vacation = 20
                return self.__message()
        if self.department_key == 2:
            if self.years == 1:
                self.vacation = 7
                return self.__message()
            elif 2 <= self.years <= 6:
                self.vacation = 15
                return self.__message()
            elif self.years >= 7:
                self.vacation = 22
                return self.__message()
        if self.department_key == 3:
            if self.years == 1:
                self.vacation = 10
                return self.__message()
            elif 2 <= self.years <= 6:
                self.vacation = 20
                return self.__message()
            elif self.years >= 7:
                self.vacation = 30
                return self.__message()

    def __message(self):
        return f"Nombre del trabajador: {self.name}\n" \
               f"Días de vacaciones: {self.vacation}"
