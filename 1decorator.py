

def outer_function():
    message = "hey now" # free variable

    def inner_function():
        print(message)
    return inner_function()

    
    
outer_function()





def outer_function():
    message = "hey now" # free variable

    def inner_function():
        print(message)
    return inner_function  # return without execution

    
# this is a closure coz it remembers message 
# variable even after outter func has finished executing
a_variable = outer_function()
a_variable()



def outer_function(msg):
    message = msg # free variable

    def inner_function():
        print(message)
    return inner_function  # return without execution

     
# this is a closure coz it remembers message 
# variable even after outter func has finished executing
hi = outer_function("ho de doh")
bye = outer_function("do de how")

hi()
bye()


def outer_function(msg):


    def inner_function():
        print(msg) #  just pass arg into print -- no need to assign
    return inner_function  # return without execution

hi = outer_function("ho de doh")
bye = outer_function("do de how")

hi()
bye()

# a decorator is a func that takes another func as argument adds some 
# kinda functionality  and returns another function
def decorator_function(original_function):
    def wrapper_function():
        return original_function()
    return wrapper_function

def display():
    print("The display function has ran")

decorated_display = decorator_function(display)    
decorated_display()


def decorator_function(original_function):

    def wrapper_function():
        print(f"wrapper exe this before this -->{original_function.__name__}")
        return original_function()
    return wrapper_function

def display():
    print("The display function has ran")

decorated_display = decorator_function(display)    
decorated_display()



def decorator_function(original_function):

    def wrapper_function():
        print(f"wrapper exe this before this -->{original_function.__name__}")
        return original_function()
    return wrapper_function


@decorator_function
def display():
    print("The display function has ran")

# decorated_display = decorator_function(display)    @decorator_function
# decorated_display()