class Employee:
    def __init__(self,name):
        self.name = name

    def name_change(self,new_name):
        self.name=new_name

    def get_name(self):
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
    def get_employees(self):
        return self.employees

emp1=Employee('Joe')
emp2=Developer('Dave','Python')
emp3=Manager('Bob',[emp2])
print(emp3.get_employees()[0].get_name())