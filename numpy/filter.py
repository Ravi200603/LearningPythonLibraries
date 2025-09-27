import numpy as np

ages = np.array([[21,22,23,24,26,30,18,65],
                [39, 22,15, 99, 18, 19, 20, 21]
                ])


# it makes new array 1d array from multi dem arrays 
teenagers = ages[ages < 19]
print("teenagers", teenagers)


adults = ages[(19 <=ages) & (ages < 65)]
print("adults", adults)

seniros = ages[(ages > 65)]
print("Seniors", seniros)


#  what if we have to preserve the original thing 

adults = np.where(ages >= 18, ages, np.nan)
print(adults)