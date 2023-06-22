names = ['larry', 'curly', 'moe', 'joe', 'frank']
cars = ['mustang', 'corvette', 'charger', 'hotbox', 'bluewind']

dct = {}
for name, car in zip(names, cars):
    dct[name] = car
print(dct)

# with a condition
cmp = {name: car for name, car in zip (names, cars) if name != 'frank'} 
print(cmp)

nums = [1,2,3,4,5,6,3,4,5,6,7,1,2,3,4,5,6,3,4,5,6,8,9,1,8,9,10]

my_set = set()
for n in nums:
    my_set.add(n)
print(my_set)    

my_set = {n for n in nums}
print(my_set)






