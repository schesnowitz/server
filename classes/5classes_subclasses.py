
class User():
    raise_amount = 1.05
    number_of_users = 0
    def __init__(self, first, last, pay):
        self.first = first  #instance variables
        self.last = last
        self.pay = pay
        self.email = f"{self.first}.{self.last}@email.com"

        User.number_of_users += 1
# a regular method
    def fullname(self):
        return '{} {}'.format(self.first, self.last)    
    

    def apply_raise(self):
        self.pay = (self.pay * self.raise_amount)
        return self.pay
    

    @classmethod
    def set_raise_ammont(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def str_to_user(cls, user_str):
        first, last, paystr = user_str.split('-')  
        pay = int(paystr)  

        return cls(first, last, pay)
    
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True
        

class Developer(User):
    raise_amount = 1.10  #  custom raise for the developers baby!
    
    def __init__(self, first, last, pay, programming_lang):
        super().__init__(first, last, pay)
        # User.__init__(self, first, last, pay) # this is also a way to do the same as aboove line
        self.programming_lang = programming_lang

class Manager(User):
    def __init__(self, first, last, pay, users=None):
        super().__init__(first, last, pay)
        # User.__init__(self, first, last, pay) # this is also a way to do the same as aboove line
        if users is None:
            self.users = []
        else:
            self.users = users    

    def add_user(self, usr):
        if usr not in self.users:
            self.users.append(usr)

    def remove_user(self, usr): 
        if usr in self.users:
            self.users.remove(usr)

    def print_users(self):
        for usr in self.users:
            print(f" ---> {usr.fullname()}")


dev_1 = Developer("Steve", "Chesnowitz", 1000, "python")    
dev_2 = Developer("Driver", "Chesnowitz", 1000, "html") 

man_1 = Manager("Sue", "Smithin", 6699, [dev_1])
# print(help(Developer))

print(man_1.email)
# print(dev_1.programming_lang)
man_1.add_user(dev_2)
man_1.print_users()
print("removed")
man_1.remove_user(dev_1)
man_1.print_users()

print(isinstance(man_1, Developer))
print(isinstance(man_1, User))
print(issubclass(Developer, User))