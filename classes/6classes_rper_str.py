
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
        return '{self.first} {self.last}'
    

    def apply_raise(self):
        self.pay = (self.pay * self.raise_amount)
        return self.pay
    
    def __repr__(self) -> str:
        return f"{self.first}, {self.last}, {self.pay}"

    def __str__(self) -> str:
        return f"{self.fullname}, {self.email}"
    
    def __add__(self, other):
        return self.pay + other.pay
    
    def __len__(self):
        return len(self.fullname())
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
        

user_1 = User("Steve", "Chesnowitz", 1000)    
user_2 = User("Driver", "Chesnowitz", 1000) 


print(user_1) 
print(len(user_1)) 
# repr(user_1)
# str(user_1)