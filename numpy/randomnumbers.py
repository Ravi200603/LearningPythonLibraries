import numpy as np 

rng = np.random.default_rng()

print(rng.integers(low= 1,high = 7, size = (3,2)))


print((np.random.uniform(0,6, (6,5))))


#  shuffling an array 

fruits = np.array(["🍎", "🍓", "🍌", "🍍", "🍊"])


fruit = rng.choice(fruits, (3,2))
print(fruit)