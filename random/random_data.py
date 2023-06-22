import random

# 0 to 1
value = random.random() * 10
print(value)

# floats
value = random.uniform(1, 10)
print(value)

# integers this is inclusive
value = random.randint(1, 10)
print(value)





# choice method picks a value from a list
vehicle = ['car', 'truck', 'boat', 'plane', 'train']
value = random.choice(vehicle)
print(value)

# key value pairs 
vehicle_kv = {'car':'car', 'truck':'truck', 'boat':'boat', 'plane':'plane', 'train':'train'}

value = random.choice(list(vehicle_kv.items())) 
value_value = random.choice(list(vehicle_kv.values())) 
print(value)
print(value_value)

colours = ["Black", "Green", "Red"]
# k value num time we want a value
value = random.choices(colours, k=10) 
print(value)
# with weights we can set odds as roulette black and red have 18 slots and green 2
value = random.choices(colours, weights=[18, 2, 18], k=10) 
print(value)

