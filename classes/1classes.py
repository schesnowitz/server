

class User():
    def __init__(self, first, last, pay) -> None:
        self.first = first  #instance variables
        self.last = last
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)    
    
user_1_info = User("Steve", "Chesnowitz", 123000)    

print(User.fullname(user_1_info))