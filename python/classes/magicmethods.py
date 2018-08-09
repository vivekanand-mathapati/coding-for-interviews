class Employee():
    def __init__(self, name, age, email, sal):
        self.name = name
        self.age = age
        self.email = email
        self.sal = sal

    def __new__(cls, *args, **kwargs):
        print("__new__ method is called")

    def __call__(self):
        print("__call__ is called")

    def __str__(self):
        return self.name

obj = Employee("vivek", 25, "v@gmail.com", 876788)
print(obj.name)