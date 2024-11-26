class Employee:

    def __init__(self,name):
        self.name = name

    def name_change(self,new_name) -> None:
        self.name=new_name

    def get_name(self) -> str:
        return self.name

class Developer(Employee):
    def __init__(self, name, lang: str):
        super().__init__(name)
        self.lang = lang

class Manager(Employee):
    def __init__(self,name,employees=None):
        super().__init__(name)
        if employees is None:
            self.employees=[]
        else:
            self.employees=employees

    def has_direct_reports(self):
        for i in self.employees:
            if i.__class__.__name__ == 'Manager':
                return True
            else:
                return False

    def get_employees(self):
        return self.employees

    def add_employees(self,emp):
        if emp not in self.employees:
            self.employees.append(emp)
        else:
            pass

    def remove_employees(self,emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_employees(self):
        for e in self.employees:
            print(e.get_name())

class Restrictions:
    pass

emp1=Employee('Joe')
emp2=Developer('Dave','Python')
emp3=Manager('Bob',[emp2])
emp4=Manager('Jill', [emp3])

all_employees = [emp1,emp2,emp3,emp4]

for e in all_employees:
    print(f'Employee Name: {e.get_name()}\nType: {e.__class__.__name__}')