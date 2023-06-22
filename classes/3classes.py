# regular, class and static methods

# regular methods in a class atomatically take self * the instance * as
# the first argument

# to make class method we add decorator to the top @classmethod
class User():

    raise_amount = 1.05
    number_of_users = 0
    def __init__(self, first, last, pay) -> None:
        self.first = first  #instance variables
        self.last = last
        self.pay = pay

        User.number_of_users += 1
# a regular method
    def fullname(self):
        return '{} {}'.format(self.first, self.last)    
    
    # class variables

    def apply_raise(self):
        self.pay = (self.pay * self.raise_amount)
        return self.pay
    

    @classmethod
    def set_raise_ammont(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def str_to_user(cls, user_str):
        first, last, pay = user_str.split('-')    

        return cls(first, last, pay)
    
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True
        
        
    
user_1_info = User("Steve", "Chesnowitz", 1000)    
user_2_info = User("Driver", "Chesnowitz", 1000) 

str_user_1 = "Frank-Smith-100"
str_user_2 = "John-Raddison-55000"
str_user_3 = "Cliff-Snoek-23000"

new_user = User.str_to_user(str_user_1)
print(f"{user_1_info.fullname()} {user_1_info.pay} {int(user_1_info.apply_raise())}")
# print(user_1_info.__dict__)
# print(User.__dict__)
# print(type(User.fullname(user_1_info)))

# print(User.number_of_users)
# print((User.apply_raise(user_1_info)))

User.set_raise_ammont(1.06)

print(User.raise_amount) # class raise amount
print(user_1_info.raise_amount) # instance 
print(user_1_info.raise_amount)

import datetime
my_date = datetime.date(2024, 7, 8)

print(User.is_workday(my_date))