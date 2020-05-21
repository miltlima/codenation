
class Department:
    def __init__(self, name, code):
        self.name = name
        self.code = code


class Employee:
    
    def __init__(self, code, name, salary):  # Proteção da classe Employee impedindo ser instanciada
        if type(self) == Employee:
            raise TypeError()
        self.code = code
        self.name = name
        self.salary = salary
        
    def get_departament(self):  # Criaçao do Metodo get_department
        return self._departament.name

    def set_departament(self, name, code):
        self._departament = Department(name, code)
        
    def get_hours(self): # Padronizaçao carga horária para todos os funcionários tornando a variável privada
        return 8

class Manager(Employee):
    def __init__(self, code, name, salary):
        super().__init__(code, name, salary)
        self._departament = Department('managers', 1)
        
    def calc_bonus(self):
        return self.salary * 0.15
    

class Seller(Employee):
    def __init__(self, code, name, salary):
        super().__init__(code, name, salary)
        self._departament = Department('sellers', 2)
        self.__sales = 0

    def get_sales(self):
        return self.__sales  # Criação metodo get_sales

    def put_sales(self, sold):
        self.__sales += sold  # Criação metodo put_sales

    def calc_bonus(self):
        return self.__sales * 0.15  # Cálculo do Bonus Vendedor sobre todas as vendas

