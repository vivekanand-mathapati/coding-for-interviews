class Employee:

    def __init__(self, name, age, sal, email):
        print("init")
        self.name = name
        self.age = age
        self.sal = sal
        self.email = email

    def __new__(cls, *args, **kwargs):
        print("new")
        return  super(Employee, cls).__new__(cls)

    def __str__(self):
        return self.name

    def foo(self):
        print("hello")

def Manager(Employee):
    

obj = Employee("vivek", 25, 25000, "vivekanand.d.mathapati@gmail.com")
print(obj.name)
obj.foo() #And Employee.foo(obj) are same
        