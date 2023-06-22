import builtins
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
    
dev_1 = Developer("Steve", "Chesnowitz", 1000)    
dev_2 = Developer("Driver", "Chesnowitz", 1000) 

str_dev_1 = "Frank-Smith-100"
new_user = Developer.str_to_user(str_dev_1)
new_user2 = User.str_to_user(str_dev_1)
# print(help(Developer))
print(new_user.pay)
new_user.apply_raise()
print(new_user.pay)


print(new_user2.pay)
new_user2.apply_raise()
print(new_user2.pay)
print(dev_2.email)
