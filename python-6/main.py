

class Department:
    def __init__(self, name, code):
        self.name = name
        self.code = code
    
class Employee:
    work_hours = 8
    def __init__(self, code, name, salary, department):
        self._code = code
        self._name = name
        self._salary = salary
        self.salary = department

class Manager(Employee):
    def __init__(self, code, name, salary, department):
        super().__init__(code, name, salary)
        self.departament = Department('managers', 1)

    def calc_bonus(self):
        return self.salary * 0.15

class Seller(Employee):
    def __init__(self, code, name, salary, sales, departament):
        super().__init__(code, name, salary)
        self.departament = Department('sellers', 2)
        self._sales += 1
    
    @staticmethod
    def get_sales(self):
        self.get_sales = self._sales
    
    def put_sales(self):
        self.put_sales += self._sales

    def calc_bonus(self):
        self.cal_bonus = get_sales * 0.15
    