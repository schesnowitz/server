nums = [1,2,3,4,5,6,7,8,9,10]


# getting n for each n in nums
a_list = []
for n in nums:
    a_list.append(n)
print(a_list)

# list comprehension
comp_list =[n for n in nums] 
print(comp_list)  

# get squary of n 
a_list = []
for n in nums:
    a_list.append(n*n)
print(a_list)    


comp_list =[n*n for n in nums] 
print(comp_list)  

# getting even n from list 

a_list = []
for n in nums:
    if n % 2 == 0:
        a_list.append(n)
print(a_list)

comp_list = [n for n in nums if n % 2 == 0]
print(comp_list)

# get a letter number pair for abcd 0123

lst = []
for letter in "abcd":
    for number in range(4):
        lst.append((letter, number))
print(lst)        


cmp = [(letter, number) for letter in 'abcd' for number in range(4)]
print(cmp)