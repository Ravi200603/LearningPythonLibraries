import numpy as np

# scaler arithmetic

array1 = np.array([1,2,3])
array2 = np.array([4,5,6])
print(array1**3)

# Vectorized math function

print(np.sqrt(array1))
print(np.pi)

radii = np.array([1,2,3])

print(np.floor((np.pi * (radii ** 2))))

print(array1 + array2)
print(array1 - array2)
print(array1 * array2)
print(array1 ** array2)
print(array1 /  array2)


# comparison operations
scores = np.array([91,55,100,73,82,64])

scores[scores <60] = 0
print(scores)