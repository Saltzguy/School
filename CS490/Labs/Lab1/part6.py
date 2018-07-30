import numpy as np


rand_array = np.random.randint(0,21,(1,15))[0] # generates a random array from 0 to 20 of size 15
freq_array = np.bincount(rand_array) # creates an array from 0 to max value in the array and counts the frequence of that value and stores the count
                                    # at an index of that value
print(freq_array)
print(rand_array)
print("The most common item in the array is " +   str(np.argmax(freq_array))) # returns the index of the max value
