class User():

    raise_amount = 1.05
    number_of_users = 0
    def __init__(self, first, last, pay) -> None:
        self.first = first  #instance variables
        self.last = last
        self.pay = pay

        User.number_of_users += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)    
    
    # class variables

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)
        return self.pay
    
user_1_info = User("Steve", "Chesnowitz", 1000)    
user_2_info = User("Driver", "Chesnowitz", 1000) 
print(user_1_info.__dict__)
print(User.__dict__)
print(type(User.fullname(user_1_info)))

print(User.number_of_users)
print((User.apply_raise(user_1_info)))